This scripts works by trying to build each and every *.spec file it finds, without knowing by advance their dependencies.
It uses mock (http://fedoraproject.org/wiki/Using_Mock_to_test_package_builds)
It's no rocket science, it's just "mechanizing" the steps you'd reproduce by hand 

Each time a RPM is succesfully built, it's saved and used for subsequent builds.
When all the *.spec files have been processed, the script loops and tries again to build the remaining packages with the ones it already built.

The script stops when no more build succeeds during the loop, which can mean two things :
	
	* all packages did build correctly
	* some packages could not be built, in this case it lists them.

Here are the basic steps :

	* make sure to edit your mock *.cfg file (found in /etc/mock/) to add this part in the "config_opts['yum.conf']" part :
		
		[buildrepo]
		name=buildrepo
		# beware : file:/// with 3 slashes
		baseurl=file:///absolute/path/to/rpms/
		enabled=1

	* Place your *.spec files in specs/ directory
	* Place source files (*.tar.gz, *.bz2 etc...) in sources/ directory
	* If any, also place patch files in sources/ directory
	* ./trybuild.php
	* if you encounter any error during build, read the logs found in rpms/PACKAGE_NAME/*.log, especially the last lines which likely will point to the error
	* try to correct errors by patching / modifying the specs / adding packages to the list
	* rinse and repeat
	