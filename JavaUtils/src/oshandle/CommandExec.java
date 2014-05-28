package oshandle;

import java.io.IOException;

/**
 * 
 * @author lucask
 *
 */
public class CommandExec {

	/**
	 * 
	 * @param commands
	 */
	public void commandArgs(String[] commands) {
		// In case developer wants to execute a command with more than
		// one argument, it is necessary to use the overload that requires
		// the command and its arguments to be supplied in an array:

		try {
			// Execute a command with an argument that contains a space
			// String[] commands = new String[]{"grep", "hello world",
			// "/tmp/f.txt"};

			// commands = new String[]{"grep",
			// "hello world","c:\\Documents and Settings\\f.txt"};

			Process child = Runtime.getRuntime().exec(commands);

		} catch (IOException e) {
		}

	}

	/**
	 * 
	 * @param command
	 */
	public void commandArgs(String command) {
		// In case developer wants to execute a command with more than
		// one argument, it is necessary to use the overload that requires
		// the command and its arguments to be supplied in an array:

		try {
			// Execute a command without arguments
			// String command = "ls";
			Process child = Runtime.getRuntime().exec(command);

			// Execute a command with an argument
			command = "ls /tmp";
			child = Runtime.getRuntime().exec(command);
		} catch (IOException e) {
		}

	}

}
