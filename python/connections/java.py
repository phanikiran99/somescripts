import subprocess
subprocess.call(["java","Test"]); #to call the standalone java class Test
subprocess.call(["java","-j","Test.jar"]); #to call the jar file Test.jar
