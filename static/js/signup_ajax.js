$(document).ready(function() {
    var signupUrl = '';

    $('#signupForm').on('submit', function(e) {
        e.preventDefault();

        $('#fullname_error').text('');
        $('#email_error').text('');
        $('#username_error').text('');
        $('#password_error').text('');
        $('#confirm_password_error').text('');
        // Validate passwords
        var password = $('#password').val();
        var confirm_password = $('#confirm_password').val();
        if (password !== confirm_password) {
         $('#confirm_password_error').text('Passwords do not match.');
            return; 
        }

        $.ajax({
            type: 'POST',
            url: signupUrl,
            data: $('#signupForm').serialize(),
            success: function(response) {
                if (response.success) {
                    alert(response.message);
                } else {
                    if (response.errors.fullname) {
                        $('#fullname_error').text(response.errors.fullname);
                    }
                    if (response.errors.email) {
                        $('#email_error').text(response.errors.email);
                    }
                    if (response.errors.username) {
                        $('#username_error').text(response.errors.username);
                    }
                    if (response.errors.password) {
                        $('#password_error').text(response.errors.password);
                    }
                }
            },
            error: function() {
                alert('An error occurred. Please try again.');
            }
        });
    });
});