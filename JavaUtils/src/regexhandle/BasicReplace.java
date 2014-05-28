package regexhandle;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class BasicReplace {
	
	public static void main(String[] args) {

		CharSequence inputStr = "p q r p q r ";
		String patternStr = "q";
		String replacementStr = "s";

		// Compile regular expression
		Pattern pattern = Pattern.compile(patternStr);

		// Replace all occurrences of pattern in input
		Matcher matcher = pattern.matcher(inputStr);
		String output = matcher.replaceAll(replacementStr);
		// p s r p s r
		System.out.println(output);
		
		String comHtml = "retirando <a href=zzz>código html</a>";
		Pattern p = Pattern.compile("<.*?>");
		Matcher m = p.matcher(comHtml);
		String semHtml = m.replaceAll("");
		System.out.println(semHtml);

	}

}
