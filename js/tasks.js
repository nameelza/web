document.addEventListener('DOMContentLoaded', function() {

    // By default, the submit button is disabled
    document.querySelector('#submit').disabled = true;

    document.querySelector('#task').onkeyup = () => {
        if (document.querySelector('#task').value.length > 0) {
            document.querySelector('#submit').disabled = false;
        } else {
            document.querySelector('#submit').disabled = true;
        }
        
    }

    document.querySelector('form').onsubmit = () => {
        const task = document.querySelector('#task').value;

        // Create a new task
        const li = document.createElement('li');
        li.innerHTML = task;

        // Add the task to the list
        document.querySelector('#tasks').append(li);

        // Clear out the input field
        document.querySelector('#task').value = "";

        // Disable the submit button
        document.querySelector('#submit').disabled = true;

        // Stop the form from submitting
        return false;
    }
});