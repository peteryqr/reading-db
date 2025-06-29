document.addEventListener('DOMContentLoaded', function() {
    const tableSelect = document.getElementById('id_table');
    const fieldSelect = document.getElementById('id_field');
    const operatorSelect = document.getElementById('id_operator');

    const userFields = [
        ['name', 'Name', 'text'],
        ['age', 'Age', 'number']
    ];

    const bookFields = [
        ['name', 'Name', 'text'],
        ['price', 'Price', 'number']
    ];

    const numericOperators = [
        ['=', 'Equals'],
        ['>', 'Greater than'],
        ['<', 'Less than'],
        ['>=', 'Greater than or equal to'],
        ['<=', 'Less than or equal to']
    ];

    const textOperators = [
        ['=', 'Equals'],
        ['contains', 'Contains']
    ];

    function updateOperatorOptions(fieldType) {
        const operators = fieldType === 'number' ? numericOperators : textOperators;
        const currentValue = operatorSelect.value;
        
        // Clear existing options
        operatorSelect.innerHTML = '';
        
        // Add new options
        operators.forEach(([value, label]) => {
            const option = document.createElement('option');
            option.value = value;
            option.textContent = label;
            // Preserve the selected value if it exists in the new options
            if (value === currentValue) {
                option.selected = true;
            }
            operatorSelect.appendChild(option);
        });
    }

    function updateFieldOptions() {
        const selectedTable = tableSelect.value;
        const fields = selectedTable === 'library_user' ? userFields : bookFields;
        const currentValue = fieldSelect.value;
        
        // Clear existing options
        fieldSelect.innerHTML = '';
        
        // Add new options
        fields.forEach(([value, label, type]) => {
            const option = document.createElement('option');
            option.value = value;
            option.textContent = label;
            option.dataset.type = type;
            // Preserve the selected value if it exists in the new options
            if (value === currentValue) {
                option.selected = true;
            }
            fieldSelect.appendChild(option);
        });

        // Update operators based on the selected field type
        const selectedOption = fieldSelect.options[fieldSelect.selectedIndex];
        const fieldType = selectedOption ? selectedOption.dataset.type : 'text';
        updateOperatorOptions(fieldType);
    }

    // Update operators when field selection changes
    fieldSelect.addEventListener('change', function() {
        const selectedOption = fieldSelect.options[fieldSelect.selectedIndex];
        const fieldType = selectedOption ? selectedOption.dataset.type : 'text';
        updateOperatorOptions(fieldType);
    });

    // Update fields when table selection changes
    tableSelect.addEventListener('change', updateFieldOptions);

    // Initial update
    updateFieldOptions();
}); 