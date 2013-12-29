import java.security.MessageDigest;
import org.eclipse.swt.*;
import org.eclipse.swt.layout.*;
import org.eclipse.swt.events.*;
import org.eclipse.swt.widgets.*;

public class Hasher {
    public static void main (String [] args) {
	Display display = new Display ();
	Shell shell = new Shell(display);

        Label label = new Label(shell, SWT.CENTER);
        label.setText("Enter a string to be hashed: ");

        final Text text = new Text(shell, SWT.BORDER);
        text.setLayoutData(new RowData(100, SWT.DEFAULT));

        Button hash = new Button(shell, SWT.PUSH);
        hash.setText("Hash Text");
        hash.addSelectionListener(new SelectionAdapter() {
                @Override
                public void widgetSelected(SelectionEvent e) {
                    MessageDigest md = null;
                    try{
                        md = MessageDigest.getInstance("SHA");
                    } catch (Exception NoSuchAlgorithmException) {
                        throw new Error("NoSuchAlgorithmException");
                    }
                    byte[] user_text = text.getText().getBytes();
                    md.update(user_text);
                    System.out.println(user_text);
                }
            });

        Button cancel = new Button(shell, SWT.PUSH);
        cancel.setText("Cancel");
        cancel.addSelectionListener(new SelectionAdapter() {
                @Override
                public void widgetSelected(SelectionEvent e) {
                    System.out.println("Cancel");
                }
            });

        shell.setDefaultButton(cancel);
        shell.setLayout(new RowLayout());
        shell.pack();
        shell.open ();
        while (!shell.isDisposed ()) {
            if (!display.readAndDispatch ()) display.sleep ();
        }
        display.dispose ();
    }
}
