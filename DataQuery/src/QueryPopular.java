import java.sql.*;

public class QueryPopular {
    public static void main (String[] args){
        try{
            String myDriver = "com.mysql.cj.jdbc.Driver";
            String myUrl = "jdbc:mysql://localhost/projectdb?useUnicode=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=GMT";
            Class.forName(myDriver);
            Connection conn = DriverManager.getConnection(myUrl, "root", "password");

            String query = "SELECT * FROM result";

            Statement st = conn.createStatement();

            ResultSet rs = st.executeQuery(query);

            while (rs.next()) {
                int resultID = rs.getInt("resultID");
                int p1Points = rs.getInt("p1Points");
                int p2Points = rs.getInt("p2Points");

                System.out.format("%s, %s, %s", resultID, p1Points, p2Points);
            }


            st.close();

        }catch (Exception e){
            System.err.println(e.getMessage());
        }
    }
}