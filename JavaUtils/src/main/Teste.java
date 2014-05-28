package main;

/**
 * Sample code that finds files that match the specified glob pattern.
 * For more information on what constitutes a glob pattern, see
 * http://docs.oracle.com/javase/tutorial/essential/io/fileOps.html#glob
 *
 * The file or directories that match the pattern are printed to
 * standard out.  The number of matches is also printed.
 *
 * When executing this application, you must put the glob pattern
 * in quotes, so the shell will not expand any wild cards:
 *              java Find . -name "*.java"
 */

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import constants.Constants;

import filehandle.FinderPattern;
import filehandle.ReadFullFile;

public class Teste {

	public static void main(String[] args) throws IOException {
		
//		FindSpecificTags tag = new FindSpecificTags(Constants.HOST+Constants.URL2);
//		
//		tag.getSegmentsLinks(tag.getAnchorTag());

//		Path startingDir = Paths.get("C:\\eclipse\\workspace\\cpm31\\acceptance.ciscoR6\\LTE\\POL-MRC-ST");
//		String pattern = "inputAvs.cfg";
//
//		// Find all files acordding a pattern
//		Finder finder = new Finder(pattern);
//		Files.walkFileTree(startingDir, finder);
//		finder.done();

		// rename files to name+".tmp"
//		for (String files : finder.getFilesNames()) {
//			System.out.println(files);
			// Obtain the reference of the existing file
//			File oldFile = new File(files);
			// Now invoke the renameTo() method on the reference, oldFile in
			// this case
//			oldFile.renameTo(new File(files + ".temp"));
//		}
		FinderPattern find = new FinderPattern();
		
		find.visitAllFiles(new File("C:\\eclipse\\workspace\\cpm31" +
				"\\acceptance.ciscoR6\\LTE\\POL-MRC-ST"));
		ArrayList<File> temp =  find.getFileList();
		
		for(File f : temp){
			System.out.println("arquivo");
			System.out.println(f.toString());
		}
		ReadFullFile read =  new ReadFullFile();
		read.readAllLines(temp.get(1));
		String teste = read.getText();
//		String pattern = "AVS::Dia-Attr-User-Equipment-Info\n*IMEISV*\n*\nEND AVS";
		String pat = "      AVS::Dia-Attr-User-Equipment-Info\n            User-Equipment-Info-Type IMEISV\n            User-Equipment-Info-Value 22 22 22 22 22 22 22 10\n      END AVS";
		System.out.println(read.getText());
		
		System.out.println(teste.replace(pat, "legal"));
		
		Pattern pattern = Pattern.compile(Constants.REGEX);
		Matcher matcher = pattern.matcher(teste);
		System.out.println(matcher.replaceAll("testando"));

	}
}