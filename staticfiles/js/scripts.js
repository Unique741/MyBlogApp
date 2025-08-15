// Dynamic search (optional enhancement for instant feedback)
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.querySelector('input[name="q"]');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            console.log('Search query:', this.value);
            // Future enhancement: AJAX search
        });
    }
});