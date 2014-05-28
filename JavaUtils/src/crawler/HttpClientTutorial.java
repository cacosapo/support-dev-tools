package crawler;

import java.io.IOException;

import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.ResponseHandler;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.BasicResponseHandler;
import org.apache.http.impl.client.DefaultHttpClient;

public class HttpClientTutorial {

	private static String host = "http://zbor.openet-telecom.lan/~tester3/newreport/";
	private static String url = "/LTE23.LTE23-011//LTE_LTE23_011.act//RunDsdUnitTests_test.dsdu_PMATF_6000000//7table1.html";

	// private static String url = "http://www.apache.org/";
	/*
	 * private static String url =
	 * "http://zbor.openet-telecom.lan/~tester3/newreport/" +
	 * "/PHONE.PHONE-AC.PHONE-AC-001//PHONE_PHONE_AC_001.act/" +
	 * "/RunDsdUnitTests_test.dsdu_PMATF_6000000/" +
	 * "RunDsdUnitTests_test.dsdu_PMATF_6000000.html";
	 */
	public static void main(String[] args) throws ClientProtocolException,
			IOException {

		HttpClient httpclient = new DefaultHttpClient();
		try {
			HttpGet httpget = new HttpGet(host+url);

			System.out.println("executing request " + httpget.getURI());

			// Create a response handler
			ResponseHandler<String> responseHandler = new BasicResponseHandler();
			String responseBody = httpclient.execute(httpget, responseHandler);
			System.out.println("----------------------------------------");
			System.out.println(responseBody);
			System.out.println("----------------------------------------");

		} finally {
			// When HttpClient instance is no longer needed,
			// shut down the connection manager to ensure
			// immediate deallocation of all system resources
			httpclient.getConnectionManager().shutdown();
		}
	}

}
