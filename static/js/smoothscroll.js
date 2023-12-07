    // Function to handle smooth scrolling
    function scrollToSection(sectionId) {
        const section = document.getElementById(sectionId);
        if (section) {
            section.scrollIntoView({ behavior: 'smooth' });
        }
    }

    // Attach click event listeners to your navigation links
    document.addEventListener('DOMContentLoaded', function () {
        const links = document.querySelectorAll('.navbar a');
        links.forEach(function (link) {
            link.addEventListener('click', function (e) {
                e.preventDefault();
                const sectionId = link.getAttribute('href').substring(1); // Remove the #
                scrollToSection(sectionId);
            });
        });
    });