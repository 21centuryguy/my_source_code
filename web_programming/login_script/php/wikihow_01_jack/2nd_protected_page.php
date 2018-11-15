<?php
include_once 'includes/db_connect.php';
include_once 'includes/functions.php';

sec_session_start();
?>
<!DOCTYPE html>

<html>
	<body>
			<?php if (login_check($mysqli) == true) : ?>
	            <p>Welcome <?php echo htmlentities($_SESSION['username']); ?>!</p>
	            <p>
	                This is the second protected page.
	            </p>
	            <p>Return to <a href="index.php">login page</a></p>
				<p>Return to <a href="protected_page.php">the first protected page</a></p>
				<p>Move to <a href="3th_protected_page.php">the third protected page</a></p>
	        <?php else : ?>
            <p>
                <span class="error">You are not authorized to access this page.</span> Please <a href="index.php">login</a>.
            </p>
        <?php endif; ?>
	</body>
</html>