package filehandle;

import java.io.File;
import java.util.ArrayList;
import java.util.regex.Pattern;

public class FinderPattern extends FinderCustom {

	private String string = "inputAvs";
	private Pattern pattern = null;
	private ArrayList<File> fileList = new ArrayList<File>();

	//
	@Override
	public void process(File dir) {
		if (dir.toString().contains(string)) {
			System.out.println("Matched: " + dir);
			fileList.add(dir);
		}
	}

	public ArrayList<File> getFileList() {
		return fileList;
	}

	public void setPattern(Pattern pattern) {
		this.pattern = pattern;
	}

	public void setString(String string) {
		this.string = string;
	}

}
