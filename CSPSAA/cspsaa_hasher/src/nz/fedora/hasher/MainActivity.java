/* 
 * 
 * Some lines of code that call Log.e are commented out. I put those in to
 * help with debugging but they serve no purpose now, feel free to uncomment them
 * if you wish.
 */

package nz.fedora.hasher;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

import org.apache.commons.codec.binary.Hex;

import android.annotation.SuppressLint;
import android.app.Activity;
import android.app.AlertDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.os.Bundle;
import android.text.ClipboardManager;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.Spinner;

@SuppressWarnings("deprecation")
public class MainActivity extends Activity {

    public final static String EXTRA_MESSAGE = "Not even sure what's going on here";
    public static String HASH_ALGO_STRING = "SHA-1";
    public static String hashedString;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
	super.onCreate(savedInstanceState);
	setContentView(R.layout.activity_main);

	// Create the spinner and it's callbacks
	final Spinner algoSpinner = (Spinner) findViewById(R.id.select_algo_spinner);
	ArrayAdapter<CharSequence> algoAdapter = ArrayAdapter.createFromResource(this, 
		R.array.algo_list,
		android.R.layout.simple_spinner_item);
	algoAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
	algoSpinner.setAdapter(algoAdapter);
	algoSpinner.setOnItemSelectedListener(
		new AdapterView.OnItemSelectedListener() {
		    @Override
		    public void onItemSelected(AdapterView<?> parent, View view, int pos, long id) {
			HASH_ALGO_STRING = parent.getItemAtPosition(pos).toString();
			// Log.e("CHNG_HASH", "Changed algorithm to " + HASH_ALGO_STRING);
		    }
		    @Override
		    public void onNothingSelected(AdapterView<?> parent) {
			// Log.e("Nothing", "Hash should be SHA-1");
		    }
		});
	algoSpinner.setSelection(1);
    }

    public void hashString(View view) {
	EditText user_string = (EditText) findViewById(R.id.text_entry_widget);
	MessageDigest digester = null;
	try {
	    digester = MessageDigest.getInstance(HASH_ALGO_STRING);
	} catch (NoSuchAlgorithmException ex) {
	    Log.e("hashStringError", "Error NoSuchAlgorithmException");
	}
	byte[] hashed_string_bytes = digester.digest(user_string.getText().toString().getBytes());
	final String hashed_string = new String(Hex.encodeHex(hashed_string_bytes));
	hashedString = hashed_string;
	// Log.e("hash", hashed_string);

	// Create a dialog to show the hashed message
	AlertDialog.Builder dialogBuilder = new AlertDialog.Builder(MainActivity.this);
	dialogBuilder.setTitle("Message Digest:");
	dialogBuilder.setMessage(hashedString);
	dialogBuilder.setPositiveButton("Copy to Clipboard", new DialogInterface.OnClickListener() {
	    @SuppressLint("NewApi")
	    @Override
	    public void onClick(DialogInterface dialog, int it) {
		int sdk_version = android.os.Build.VERSION.SDK_INT;
		if (sdk_version < android.os.Build.VERSION_CODES.HONEYCOMB) {
		    ClipboardManager clipboard = (ClipboardManager) getSystemService(Context.CLIPBOARD_SERVICE);
		    clipboard.setText(hashed_string);
		} else {
		    android.content.ClipboardManager clipboard = (android.content.ClipboardManager) getSystemService(Context.CLIPBOARD_SERVICE);
		    android.content.ClipData digest = android.content.ClipData.newPlainText("MsgDigest", hashed_string);
		    clipboard.setPrimaryClip(digest);
		}
		// Log.e("COPY", "Now to implement a copy to clipboard");
	    }
	});
	dialogBuilder.setNegativeButton("Close", new DialogInterface.OnClickListener() {
	    @Override
	    public void onClick(DialogInterface dialog, int which) {
		// Log.e("CLOSED_DIALOG", "DIALOG CLOSED!");
		dialog.cancel();
	    }
	});
	dialogBuilder.show();
    }
}