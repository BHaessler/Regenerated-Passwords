document.getElementById('passwordForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const numberOfPasswords = parseInt(document.getElementById('number').value);
    const lengthOfPasswords = parseInt(document.getElementById('length').value);
    const difficulty = document.getElementById('difficulty').value.toLowerCase();
    
    // Check for negative numbers
    if (numberOfPasswords < 1) {
        alert('Please enter a positive number for the number of passwords.');
        return;
    }
    
    if (lengthOfPasswords < 1) {
        alert('Please enter a positive number for the length of passwords.');
        return;
    }

    // Difficulty validation
    if (!['e', 'm', 'h'].includes(difficulty)) {
        alert('Invalid difficulty! Please enter E, M, or H.');
        return;
    }

    const passwords = generatePasswords(numberOfPasswords, lengthOfPasswords, difficulty);
    
    document.getElementById('passwordsOutput').textContent = passwords.join('\n');
    document.getElementById('downloadBtn').style.display = 'block';
});

function generatePasswords(num, length, difficulty) {
    const charSets = {
        e: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        m: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
        h: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~`!@#$%^&*?/ ",
    };

    const charList = charSets[difficulty] || charSets.e; // Default to easy if invalid difficulty
    const passwords = [];
    
    for (let i = 0; i < num; i++) {
        let password = '';
        for (let j = 0; j < length; j++) {
            password += charList.charAt(Math.floor(Math.random() * charList.length));
        }
        passwords.push(password);
    }
    
    return passwords;
}

document.getElementById('downloadBtn').addEventListener('click', function() {
    const passwords = document.getElementById('passwordsOutput').textContent;
    const blob = new Blob([passwords], { type: 'text/plain' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'passwords.txt';
    link.click();
});