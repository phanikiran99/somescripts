package pyTest;

import java.io.IOException;
import java.lang.ProcessBuilder.Redirect;
public class Pythonj {

	public static void main(String[] args) throws IOException, Exception {
		
		
		System.out.println("Testing Jar From Python");
		System.out.println(System.getProperty("user.dir"));
		
		ProcessBuilder pb = new ProcessBuilder("python", "src\\pyTest\\script.py","");
		pb.redirectOutput(Redirect.INHERIT);
		Process p = pb.start();
		p.waitFor();
		System.out.println("Testing Jar From Python done");
 }
}
