#!/usr/bin/php
<?php

chdir(__DIR__);
$thisdir = rtrim(__DIR__, '/');


function system_exception($pCmd) {
	$ret = system($pCmd, $returnVal);
	if($returnVal != 0) {
		throw new Exception("$pCmd exited with non zero ($returnVal) value");
	}
	return $ret;
}


$specFiles = glob('specs/*.spec');

foreach($specFiles as $specFile) {
	$specName = basename($specFile);
	$packageName = preg_replace('#\.spec$#', '', $specName);
	
	$specMd5 = md5_file($specFile);
		
	if(!file_exists('intermediates/'.$packageName.'/spec.md5') || file_get_contents('intermediates/'.$packageName.'/spec.md5') != $specMd5) {
		
		echo "building SRPM for ".$packageName." ... \n";
		
		if(!is_dir('intermediates/'.$packageName)) {
			mkdir('intermediates/'.$packageName);
		}
		
		try {
			system_exception('find  "intermediates/'.$packageName.'" -type f -name "*" -exec rm "{}" \;');
			system_exception('find  "buildresult/" -type f -name "*" -exec rm "{}" \;');
			
			system_exception('mock -q --buildsrpm --sources "'.__DIR__.'/sources/" --resultdir "'.__DIR__.'/buildresult/" --spec "'.__DIR__.'/'.$specFile.'"');
			system_exception('find "buildresult/" -type f -name "*.src.rpm" -exec mv "{}" "intermediates/'.$packageName.'" \;');
			
			file_put_contents('intermediates/'.$packageName.'/spec.md5', $specMd5);
			echo "\tOK\n";
		} catch (Exception $e) {
			
			exec('find "buildresult/" -type f -name "*.log" -exec mv "{}" "intermediates/'.$packageName.'" \;');
			echo "\tFAILED\n";
		}
	}
}




if(!file_exists('buildorder.boost')) {
	
	$buildOrder  = "# This file contains package names in the order they were built"."\n";
	$buildOrder .= "# it is only used to boost build speed and can safely be removed"."\n";
	$buildOrder .= "# it will be recreated on subsequent calls"."\n";

	file_put_contents('buildorder.boost', $buildOrder);
}



$lastErrors = null;
$built = 0;



do {
	
	
	
	$builtThisLoop = 0;
	
	$continue = true;
	
	$notBuilt = array();
	
	
	// grab all rpms that don't seem to be built
	$SRPMS = glob('intermediates/*/*.src.rpm');

	$toBuild = array();
	foreach($SRPMS as $SRPM) {
		
		$path = pathinfo($SRPM);
		$package = preg_replace('#^intermediates/#', '', $path['dirname']);
		
		$specMd5 = md5_file('specs/'.$package.'.spec');
		
		if(!is_dir('rpms/'.$package)) {
			mkdir('rpms/'.$package);
		}
		
		if(!file_exists('rpms/'.$package.'/spec.md5') || file_get_contents('rpms/'.$package.'/spec.md5') != $specMd5) {
			$toBuild[$package] = $SRPM;
		}
	}
	
	
	if(count($toBuild) == 0) {
		echo "No more package found for building\n";
		$continue = false;
	
	} else {
		
		file_put_contents('buildorder.boost', file_get_contents('buildorder.boost').'# build '.date('Y-m-d H:i:s')."\n");
		
		echo "Found ".count($toBuild)." waiting for building, proceeding ... \n";
		
		// let's order them so as to boost build process
		$buildBoost = file('buildorder.boost');
		foreach ($buildBoost as $key => $value) {
			$buildBoost[$key] = trim($value);
		}
		
		uksort($toBuild, function ($p1, $p2) {
			global $buildBoost;
			$positionP1 = array_search($p1, $buildBoost);
			$positionP2 = array_search($p2, $buildBoost);
			
			
			if($positionP1 === false) {
				$positionP1 = count($buildBoost) + 1;
			}
			if($positionP2 === false) {
				$positionP2 = count($buildBoost) + 1;
			}
			return $positionP1 - $positionP2;
		});
				
		
		// they are now ordered, let's go !
		foreach($toBuild as $packageName => $srpm) {
			
			$lignes = array();
			
			
			echo "building Binary for ".$packageName." ... \n";
			
			try {
				system_exception('find  "rpms/'.$packageName.'" -type f -name "*" -exec rm "{}" \;');
				system_exception('find  "buildresult/" -type f -name "*" -exec rm "{}" \;');
			
				system_exception('mock -q --rebuild --resultdir "'.__DIR__.'/buildresult/" "'.__DIR__.'/'.$srpm.'"');
				
				system_exception('find "buildresult/" -type f -name "*.rpm" -exec mv "{}" "rpms/'.$packageName.'" \;');
				
				system_exception('createrepo rpms');
				
				$specMd5 = md5_file('specs/'.$packageName.'.spec');
				file_put_contents('rpms/'.$packageName.'/spec.md5', $specMd5);
				file_put_contents('buildorder.boost', file_get_contents('buildorder.boost').$packageName."\n");
			
				$builtThisLoop++;
				echo "\tOK\n";
			} catch (Exception $e) {
				
				exec('find "buildresult/" -type f -name "*.log" -exec mv "{}" "rpms/'.$packageName.'" \;');
				$notBuilt[] = $packageName;
				echo "\tFailed\n";
			}
			
		}
		
		
		$built += $builtThisLoop;
	
	
		if($builtThisLoop == 0) {
			echo "Could not build any more package, exiting\n";
			
			if(count($notBuilt) > 0) {
				$sortie = "The following packages could not be built :\n";
				echo implode("\n", $notBuilt)."\n";
			}
			
			$continue = false;
		
		} else {
			echo "Built ".$builtThisLoop." packages out of ".count($toBuild).", let's try again\n\n";
		}
	}
	
} while($continue == true);


