package propertieshandle;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;

public class PropertiesReader {

	public static void main(String[] args) throws IOException {
		// o arquivo encontra-se no mesmo diretório //da aplicação
		File file = new File("properties/config.properties");
		Properties props = new Properties();
		FileInputStream fis = null;
		try {
			fis = new FileInputStream(file);
			// lê os dados que estão no arquivo
			props.load(fis);
			System.out.println(props.getProperty("teste"));
			fis.close();
		} catch (IOException ex) {
			System.out.println(ex.getMessage());
			ex.printStackTrace();
		}

	}
}
