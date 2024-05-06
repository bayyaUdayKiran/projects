import java.awt.*;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.*;

public class Server extends JFrame implements ActionListener{
    Server(){

        
        setLayout(null);
        
        //Header..
        JPanel header = new JPanel();
        header.setBackground(new Color(219, 175, 53));
        header.setBounds(0, 0, 450, 65);
        header.setLayout(null);
        add(header);

        ImageIcon imgBackTick = new ImageIcon(ClassLoader.getSystemResource("res/back-tick.png"));
        Image backTick = imgBackTick.getImage().getScaledInstance(25, 25, Image.SCALE_DEFAULT);
        ImageIcon theBackTick = new ImageIcon(backTick);
        JLabel back = new JLabel(theBackTick);
        back.setBounds(5, 20, 25, 25);
        header.add(back);
        back.addMouseListener(new MouseAdapter() {
            public void mouseClicked(MouseEvent ae){
                setVisible(false);
            }
        });

        //Frame..
        setSize(450, 700);
        
        getContentPane().setBackground(Color.black);

        setLocation(200, 5);

        setVisible(true);


        public void actionPerformed(ActionEvent ae){


        }

        
        
    }

    public static void main(String[] args) {
        new Server();
    }

    




}