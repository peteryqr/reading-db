document.addEventListener('DOMContentLoaded', function() {
    const tableSelect = document.getElementById('id_table');
    const fieldSelect = document.getElementById('id_field');

    const userFields = [
        ['name', 'Name'],
        ['age', 'Age']
    ];

    const bookFields = [
        ['name', 'Name'],
        ['price', 'Price']
    ];

    function updateFieldOptions() {
        const selectedTable = tableSelect.value;
        const fields = selectedTable === 'library_user' ? userFields : bookFields;
        
        // Clear existing options
        fieldSelect.innerHTML = '';
        
        // Add new options
        fields.forEach(([value, label]) => {
            const option = document.createElement('option');
            option.value = value;
            option.textContent = label;
            fieldSelect.appendChild(option);
        });
    }

    // Update fields when table selection changes
    tableSelect.addEventListener('change', updateFieldOptions);

    // Initial update
    updateFieldOptions();
}); 