package regexhandle;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

import constants.Constants;

public class RegexCustom {

	private Pattern pattern = null;
	private Matcher matcher = null;
	private String text = "";

	public String replacePattern(String replace) {
		pattern = Pattern.compile(Constants.REGEX);
		matcher = pattern.matcher(text);
		return matcher.replaceAll(replace);
	}

}
