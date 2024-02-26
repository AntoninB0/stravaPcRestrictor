function submit_js() {
    var time = document.getElementById('timeRestrict').value
    var days = [document.getElementById('Monday').checked, document.getElementById('Tuesday').checked, document.getElementById('Wednesday').checked, document.getElementById('Thursday').checked, document.getElementById('Friday').checked, document.getElementById('Saturday').checked, document.getElementById('Sunday').checked]
    var connexion = [document.getElementById('Credential').value, document.getElementById('Password').value]
    eel.submit_py(time,days,connexion);
}

        