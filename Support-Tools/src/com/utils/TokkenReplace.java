package com.utils;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class TokkenReplace {
	
	
	// String list that will replace the tokken
	private static String[] list = {"omsAcvtive","pcAcvtive","printerAcvtive","refrigeratorAcvtive","tcAcvtive","vcAcvtive",
			"wmAcvtive","acAcvtive","acSolAcvtive","acSyeAcvtive","a3CopierAcvtive","apsAcvtive",
			"avAcvtive","bdAcvtive","camAcvtive","dgcAcvtive","dscAcvtive","dvdAcvtive","dwAcvtive",
			"faxMFPAcvtive","lensAcvtive","midAcvtive","monitorAcvtive","mobileAcvtive","mwoAcvtive",
			"miniMicroAcvtive","htsAcvtive"};
	

	// String list that will replace the tokken
	private static ArrayList<String> stringList = new ArrayList<String>(); 
	/**
	 * Replace a tokken in order to create a new command or line to be inserted in a file
	 * P.S: Cornojob
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args) throws IOException {
//		String template = "var #TOKKEN#           	= $(\"select[name=in_#TOKKEN#]\").val();\n";
//		partnerSiteMaster.setAcAcvtive((excelRow.get("ac_acvtive") == null) ? "0" : excelRow.get("acAcvtive").toString());
		String template = "params['datas[0].#TOKKEN#']\t\t\t= #TOKKEN#;\n";
		
		File input = new File("input.txt");
		File output = new File("output.txt");
		if (!input.exists()) input.createNewFile();
		if (!output.exists()) output.createNewFile();
//		FileInputStream fin =  new FileInputStream(input);
//		FileOutputStream  fout =  new FileOutputStream(output);
		FileReader fread = new FileReader(input);
		BufferedReader bfr = new BufferedReader(fread);
		String line;
		while( (line = bfr.readLine()) != null){
			stringList.add(line.trim());
		}
		
		FileWriter fwrt = new FileWriter(output);
		
//		for (String temp : list) {
//			fwrt.append(template.replaceAll("#TOKKEN#", temp));
//		}
		for (String temp : stringList) {
			fwrt.append(temp.replaceAll("Acvtive", ""));
		}
		bfr.close();
		fread.close();
		fwrt.close();
	}
}
