import javax.swing.SwingUtilities;

public class GripperApp {

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new GripperUI());
    }
}
