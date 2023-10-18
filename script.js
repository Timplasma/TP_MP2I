function toggleFiles(rubriqueId) {
    const fileContainer = document.getElementById(`files${rubriqueId.slice(-1)}`);
    if (fileContainer.style.display === 'none' || fileContainer.style.display === '') {
        fileContainer.style.display = 'block';
    } else {
        fileContainer.style.display = 'none';
    }
}
