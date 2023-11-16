import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.text.NumberFormat;
import java.util.HashMap;
import java.util.Locale;
import java.util.Map;

public class VendingMachineGUI {
    private Map<String, Integer> inventory;
    private Map<String, Integer> productQuantity;
    private int balance;

    private JFrame frame;
    private JTextField balanceField;
    private JTextArea productArea;
    private JTextArea purchaseSummaryArea;  // Added a new JTextArea for purchase summary
    private JTextField coinField;
    private JTextField purchaseField;
    private JTextField quantityField;
    private JButton purchaseButton;

    public VendingMachineGUI() {
        inventory = new HashMap<>();
        productQuantity = new HashMap<>();
        balance = 0;

        frame = new JFrame("Vending Machine");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);  // Increased frame height to accommodate new section

        frame.getContentPane().setBackground(new Color(255, 255, 204)); // Light yellow background
        frame.getContentPane().setForeground(Color.BLACK);

        JPanel inputPanel = new JPanel();
        balanceField = new JTextField("Balance: ₹0.00", 10);
        coinField = new JTextField(5);
        coinField.setBackground(Color.WHITE);
        JButton insertCoinButton = new JButton("Insert Coin");
        insertCoinButton.setBackground(Color.GREEN);
        insertCoinButton.setForeground(Color.WHITE);

        inputPanel.add(balanceField);
        inputPanel.add(coinField);
        inputPanel.add(insertCoinButton);

        productArea = new JTextArea(10, 30);
        productArea.setEditable(false);
        productArea.setBackground(new Color(255, 255, 204)); // Light yellow background
        productArea.setForeground(Color.BLUE);

        purchaseSummaryArea = new JTextArea(5, 30);
        purchaseSummaryArea.setEditable(false);
        purchaseSummaryArea.setBackground(new Color(255, 255, 204)); // Light yellow background
        purchaseSummaryArea.setForeground(Color.RED);

        JPanel purchasePanel = new JPanel();
        JLabel purchaseLabel = new JLabel("Enter Product Name:");
        JLabel quantityLabel = new JLabel("Enter Quantity:");

        purchaseField = new JTextField(10);
        purchaseField.setBackground(Color.WHITE);

        quantityField = new JTextField(5);
        quantityField.setBackground(Color.WHITE);

        purchaseButton = new JButton("Purchase");
        purchaseButton.setBackground(Color.PINK);
        purchaseButton.setForeground(Color.WHITE);

        purchasePanel.add(purchaseLabel);
        purchasePanel.add(purchaseField);
        purchasePanel.add(quantityLabel);
        purchasePanel.add(quantityField);
        purchasePanel.add(purchaseButton);

        frame.add(inputPanel, BorderLayout.NORTH);
        frame.add(new JScrollPane(productArea), BorderLayout.CENTER);
        frame.add(purchasePanel, BorderLayout.SOUTH);
        frame.add(new JScrollPane(purchaseSummaryArea), BorderLayout.EAST);  // Added a new JScrollPane for purchase summary

        insertCoinButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                insertCoin(Integer.parseInt(coinField.getText()));
                coinField.setText("");
            }
        });

        purchaseButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String product = purchaseField.getText();
                int quantity = Integer.parseInt(quantityField.getText());
                purchaseProduct(product, quantity);
                purchaseField.setText("");
                quantityField.setText("");
            }
        });

        frame.setVisible(true);
    }

    public void addProduct(String product, int price, int quantity) {
        inventory.put(product, price);
        productQuantity.put(product, quantity);
    }

    public void insertCoin(int coin) {
        balance += coin;
        updateBalanceField();
    }

    public void displayProducts() {
        productArea.setText("Available Products:\n");
        for (String product : inventory.keySet()) {
            int price = inventory.get(product);
            int quantity = productQuantity.get(product);
            productArea.append(product + " - ₹" + formatCurrency(price) + " (Quantity: " + quantity + ")\n");
        }
    }

    public void purchaseProduct(String product, int quantity) {
        if (inventory.containsKey(product)) {
            int price = inventory.get(product);
            int currentQuantity = productQuantity.get(product);
            if (currentQuantity >= quantity) {
                int totalPrice = price * quantity;
                if (balance >= totalPrice) {
                    productArea.append("You purchased " + quantity + " " + product + " for ₹" + formatCurrency(totalPrice) + "\n");

                    // New section to show the name and quantity of the purchased product in the summary
                    purchaseSummaryArea.append("Purchase Summary:\n");
                    purchaseSummaryArea.append("Product: " + product + "\n");
                    purchaseSummaryArea.append("Quantity: " + quantity + "\n");
                    purchaseSummaryArea.append("Total Price: ₹" + formatCurrency(totalPrice) + "\n");

                    balance -= totalPrice;
                    currentQuantity -= quantity;
                    productQuantity.put(product, currentQuantity);
                    updateBalanceField();
                } else {
                    productArea.append("Insufficient balance. Please insert more coins.\n");
                }
            } else {
                productArea.append("Not enough " + product + " in stock.\n");
            }
        } else {
            productArea.append("Product not found.\n");
        }
    }

    private void updateBalanceField() {
        balanceField.setText("Balance: ₹" + formatCurrency(balance));
    }

    private String formatCurrency(int amount) {
        NumberFormat format = NumberFormat.getCurrencyInstance(new Locale("en", "IN"));
        return format.format(amount);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            VendingMachineGUI vendingMachine = new VendingMachineGUI();
            vendingMachine.addProduct("Soda", 20, 10);
            vendingMachine.addProduct("Chips", 10, 15);
            vendingMachine.addProduct("Candy", 10, 20);
            vendingMachine.addProduct("Cookies", 10, 10);
            vendingMachine.addProduct("Cake", 10, 10);
            vendingMachine.addProduct("Juice", 20, 10);
            vendingMachine.displayProducts();
        });
    }
}
