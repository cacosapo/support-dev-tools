package codereview.handlers;

import org.eclipse.core.commands.AbstractHandler;
import org.eclipse.core.commands.ExecutionEvent;
import org.eclipse.core.commands.ExecutionException;
import org.eclipse.core.runtime.Preferences;
import org.eclipse.jface.dialogs.MessageDialog;
import org.eclipse.ui.IWorkbenchWindow;
import org.eclipse.ui.handlers.HandlerUtil;
import org.eclipse.ui.internal.wizards.preferences.PreferencesContentProvider;

import codereview.Activator;
import codereview.preferences.PreferenceConstants;

/**
 * Our sample handler extends AbstractHandler, an IHandler base class.
 * @see org.eclipse.core.commands.IHandler
 * @see org.eclipse.core.commands.AbstractHandler
 */
public class CodeReviewHandler extends AbstractHandler {
	/**
	 * The constructor.
	 */
	public CodeReviewHandler() {
	}

	/**
	 * the command has been executed, so extract extract the needed information
	 * from the application context.
	 */
	public Object execute(ExecutionEvent event) throws ExecutionException {
		IWorkbenchWindow window = HandlerUtil.getActiveWorkbenchWindowChecked(event);
		
		Preferences prefs = Activator.getDefault().getPluginPreferences();
		String value = prefs.getString(PreferenceConstants.P_STRING);
		
		
		MessageDialog.openInformation(
				window.getShell(),
				"CodeReview",
				"Hello, Eclipse world " + value);
		return null;
	}
}
