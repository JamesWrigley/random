import org.eclipse.swt.*;
import org.eclipse.swt.layout.*;
import org.eclipse.swt.events.*;
import org.eclipse.swt.widgets.*;
import javax.xml.bind.DatatypeConverter;
import java.security.MessageDigest;

public class Hasher {
    public static void main (String [] args) {
	Display display = new Display ();
	final Shell shell = new Shell(display);
        shell.setSize(435, 100);

        GridLayout layout = new GridLayout(4, false);
        shell.setLayout(layout);
        GridData grid_data = new GridData();
        grid_data.horizontalAlignment = SWT.FILL;

        final Combo algo_combo_box = new Combo(shell, SWT.READ_ONLY);
        algo_combo_box.setItems(new String[] {"MD2", "MD5", "SHA-1", "SHA-256", "SHA-384", "SHA-512"});
        algo_combo_box.select(2);
        algo_combo_box.setLayoutData(grid_data);

        Label label = new Label(shell, SWT.CENTER);
        label.setText("Enter a string to be hashed: ");
        label.setLayoutData(new GridData());

        final Text text = new Text(shell, SWT.BORDER);
        text.setLayoutData(new RowData(100, SWT.DEFAULT));
        text.setLayoutData(grid_data);

        Button hash = new Button(shell, SWT.PUSH);
        hash.setText("Hash Text");
        hash.addSelectionListener(new SelectionAdapter() {
                @Override
                public void widgetSelected(SelectionEvent e) {
                    MessageDigest md = null;
                    try{
                        md = MessageDigest.getInstance(algo_combo_box.getText());
                    } catch (java.security.NoSuchAlgorithmException ex) {
                        throw new Error("Algorithm not found");
                    }
                    String user_text_digest = DatatypeConverter.printHexBinary(md.digest(text.getText().getBytes()));

                    MessageBox digest_dialog = new MessageBox(shell, SWT.OK | SWT.CLOSE);
                    digest_dialog.setText("Hash Output");
                    digest_dialog.setMessage(user_text_digest.toLowerCase());
                    digest_dialog.open();
                }
            });
        hash.setLayoutData(new GridData());

        Button exit_button = new Button(shell, SWT.PUSH);
        exit_button.setText("Exit");
        exit_button.addSelectionListener(new SelectionAdapter() {
                @Override
                public void widgetSelected(SelectionEvent e) {
                    System.exit(0);
                }
            });
        exit_button.setLayoutData(new GridData(SWT.RIGHT, SWT.BOTTOM, true, true, 4, 1));

        shell.setDefaultButton(hash);
        shell.open();
        while (!shell.isDisposed()) {
            if (!display.readAndDispatch()) display.sleep();
        }
        display.dispose();
    }
}
