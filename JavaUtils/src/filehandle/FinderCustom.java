package filehandle;

import java.io.File;

/**
 * Find a specific file or dir or both in a dir
 * 
 * @author lucask
 * 
 */
public class FinderCustom {

	/**
	 * Process all files and directories under dir
	 * 
	 * @param dir
	 */
	public void visitAllDirsAndFiles(File dir) {
		process(dir);

		if (dir.isDirectory()) {
			for (String children : dir.list()) {
				visitAllDirsAndFiles(new File(dir, children));
			}
		}
	}

	/**
	 * Process only directories under dir
	 * 
	 * @param dir
	 */
	public void visitAllDirs(File dir) {
		if (dir.isDirectory()) {
			process(dir);

			for (String children : dir.list()) {
				visitAllDirs(new File(dir, children));
			}
		}
	}

	/**
	 * 
	 * @param dir
	 */
	public void process(File dir) {
		System.out.println("Matched: " + dir);
	}

	/**
	 * Process only files under dir
	 * 
	 * @param dir
	 */
	public void visitAllFiles(File dir) {
		if (dir.isDirectory()) {
			for (String children : dir.list()) {
				visitAllFiles(new File(dir, children));
			}
		} else {
			process(dir);
		}
	}

}
