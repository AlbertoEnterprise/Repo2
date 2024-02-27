import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Main {
    private static final String DB_URL = "jdbc:mysql://localhost:3306/mydatabase";
    private static final String DB_USER = "root";
    private static final String DB_PASSWORD = "password";

    public static void main(String[] args) {
        String username = args[0]; // Vulnerabilidad de entrada de usuario
        String password = args[1]; // Vulnerabilidad de entrada de usuario

        Connection connection = null;
        PreparedStatement statement = null;
        ResultSet resultSet = null;

        try {
            // Establecer conexión con la base de datos
            connection = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);

            // Crear la consulta SQL concatenando los valores del usuario (Vulnerabilidad de SQL Injection)
            String sql = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'";
            statement = connection.prepareStatement(sql);

            // Ejecutar la consulta
            resultSet = statement.executeQuery();

            // Procesar los resultados
            if (resultSet.next()) {
                System.out.println("Inicio de sesión exitoso para el usuario: " + username);
            } else {
                System.out.println("Inicio de sesión fallido. Usuario no encontrado.");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            // Cerrar conexiones
            try {
                if (resultSet != null) resultSet.close();
                if (statement != null) statement.close();
                if (connection != null) connection.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
