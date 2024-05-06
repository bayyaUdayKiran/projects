import java.io.*;
import javax.swing.*;
public class Test {
    public static void main(String[] args) {
        JFrame frame = new JFrame();
        JButton button = new JButton("Click");
        button.setBounds(155, 260, 200, 65);
        frame.add(button);
        frame.setSize(500, 600);
        frame.setLayout(null);
        frame.setVisible(true);

    }
}
