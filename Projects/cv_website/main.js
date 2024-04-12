


// Toggle Full Text Function
function toggleFullText() {
    var shortText = document.getElementById("shortText");
    var fullText = document.getElementById("fullText");
    var toggleButton = document.getElementById("toggleButton");

    if (fullText.style.display === "none") {
        fullText.style.display = "block";
        shortText.style.display = "none";
        toggleButton.innerText = "Less";
    } else {
        fullText.style.display = "none";
        shortText.style.display = "block";
        toggleButton.innerText = "More";
    }
}
document.addEventListener('DOMContentLoaded', function() {
    // Combined functionality for DOMContentLoaded

    // Typing Animation
    const texts = ["Salut", "Ciao", "Hoi", "Hi! I'm Jean"];
    let count = 0;
    let index = 0;
    let currentText = '';
    let letter = '';

    (function type() {
        if (count === texts.length) {
            count = 0; // Corrected reset count
        }
        currentText = texts[count];
        letter = currentText.slice(0, ++index);

        document.querySelector('.animation-text-block').textContent = letter;
        if (letter.length === currentText.length) {
            count++;
            index = 0;
            setTimeout(type, 2000); // Delay before starting next text
        } else {
            setTimeout(type, currentText.length === letter.length ? 800 : 200); // Longer delay at the end of each word
        }
    }());

    // URL Hash Replacement
    if (window.location.hash !== '#first-page') {
        history.replaceState(null, null, window.location.pathname + '#first-page');
        window.location.reload();
    }
});


window.onload = function() {
    // Replace the current URL with the base URL and add #first-page hash
    history.replaceState(null, null, window.location.pathname + '#first-page');

    // Your existing onload functionality for toggling text
    var fullText = document.getElementById("fullText");
    var shortText = document.getElementById("shortText");
    fullText.style.display = "none";
    shortText.style.display = "block";
};

document.addEventListener('scroll', function() {
    var scrollPosition = window.scrollY;
    var windowHeight = window.innerHeight;
    
    // Adjust these selectors based on your HTML structure
    var separators = document.querySelectorAll('.title-separator');

    separators.forEach(function(separator) {
        var separatorPosition = separator.getBoundingClientRect().top + scrollPosition;
        
        if (scrollPosition + windowHeight > separatorPosition) {
            separator.style.width = '100%'; // Full width when the separator is in view
        } else {
            separator.style.width = '0'; // Reset when not in view
        }
    });
});

document.addEventListener('scroll', function() {
    var sections = document.querySelectorAll('section');
    var currentSectionText = ''; // Variable to store the active section text

    sections.forEach(function(section) {
        var sectionPosition = section.getBoundingClientRect().top;

        if (sectionPosition < window.innerHeight / 2 && sectionPosition > -window.innerHeight / 2) {
            currentSectionText = section.getAttribute('data-rolling-text'); // Assuming each section has a data-rolling-text attribute
        }
    });

    // Update the text display element with the current section text
    document.getElementById('rolling-text-display').textContent = currentSectionText;
});

