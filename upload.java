import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

public class upload{
    /*public static void main(String[] args) throws Exception{

        File fileToUpload = new File("C:\\chosun.jfif");

        URL url = new URL("https://api.imgbb.com/1/upload");
        HttpURLConnection con = (HttpURLConnection) url.openConnection();

        con.setRequestMethod("POST");
        con.setRequestProperty("Content-Type", "application/json; utf-8");
        con.setRequestProperty("Accept", "application/json");
        con.setDoOutput(true);

        String jsonInpuString = "{}";

        try(OutputStream os = con.getOutputStream()){
            byte[] input = jsonInpuString.getBytes("utf-8");
            os.write(input, 0, input.length);
        }

        try(BufferedReader br = new BufferedReader(new InputStreamReader(con.getInputStream(),"utf-8"))){
            StringBuilder response = new StringBuilder();
            String responseLine = null;
            while((responseLine = br.readLine())!=null){
                response.append(responseLine.trim());
            }
            System.out.println(response.toString());
        }
    }*/

    public static String postRequest(String pURL, String pkey, String img){
        String myResult = "";

        try { 
            URL url = new URL(pURL);

            HttpURLConnection http = (HttpURLConnection) url.openConnection(); 
            
            http.setDefaultUseCaches(false);
            http.setDoInput(true); 
            http.setDoOutput(true);  
            http.setRequestMethod("POST");

            http.setRequestProperty("content-type", "application/x-www-form-urlencoded");

            StringBuffer buffer = new StringBuffer();

            buffer.append("key=").append(pkey).append(" & image=").append(img).append("\n");

            OutputStreamWriter outStream = new OutputStreamWriter(http.getOutputStream(), "UTF-8");
            PrintWriter writer = new PrintWriter(outStream);
            writer.write(buffer.toString());
            writer.flush();

            InputStreamReader tmp = new InputStreamReader(http.getInputStream(), "UTF-8");
            BufferedReader reader = new BufferedReader(tmp);
            StringBuilder builder = new StringBuilder();
            String str;
            while ((str = reader.readLine()) != null) {
                builder.append(str + "\n");
            }
            myResult = builder.toString();
            return myResult;

        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println(myResult);
        return myResult;
    }
}