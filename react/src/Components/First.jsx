import React, { useEffect, useState } from 'react';

const First = () => {
    const [tables, setTables] = useState([]); // List of tables
    const [columns, setColumns] = useState([]); // List of columns based on selected table
    const [columnData, setColumnData] = useState([]); // Data to show for selected column
    const [selectedTable, setSelectedTable] = useState(""); // Selected table
    const [selectedColumn, setSelectedColumn] = useState(""); // Selected column

    // Fetch tables and columns from the backend when the component mounts
    useEffect(() => {
        fetch('http://localhost:5000/api/tables')
            .then(response => response.json())
            .then(data => {
                setTables(data);
            })
            .catch(error => console.log('Error fetching tables:', error));
    }, []);

    // Handle table selection
    const handleTableSelect = (event) => {
        setSelectedTable(event.target.value);
        if (event.target.value) {
            const columns = tables[event.target.value]?.columns || [];
            setColumns(columns);
        }
    };

    // Handle column selection
    const handleColumnSelect = (event) => {
        setSelectedColumn(event.target.value);
    };

    // Fetch data for the selected column
    const handleButtonClick = () => {
        if (selectedTable && selectedColumn) {
            fetch(`http://localhost:5000/api/column_data?table=${selectedTable}&column=${selectedColumn}`)
                .then(response => response.json())
                .then(data => setColumnData(data))
                .catch(error => console.log('Error fetching column data:', error));
        }
    };

    return (
        <div>
            <h1>Database Tables and Columns</h1>

            {/* Dropdown for table selection */}
            <select onChange={handleTableSelect} value={selectedTable}>
                <option value="">Select a table</option>
                {Object.keys(tables).map((table, index) => (
                    <option key={index} value={table}>
                        {table}
                    </option>
                ))}
            </select>

            {/* Dropdown for column selection */}
            {selectedTable && (
                <select onChange={handleColumnSelect} value={selectedColumn}>
                    <option value="">Select a column</option>
                    {columns.map((column, index) => (
                        <option key={index} value={column}>
                            {column}
                        </option>
                    ))}
                </select>
            )}

            {/* Button to fetch column data */}
            <button onClick={handleButtonClick}>Show Data</button>

            {/* Show column data */}
            {columnData.length > 0 && (
                <div>
                    <h2>Data for Column: {selectedColumn}</h2>
                    <ul>
                        {columnData.map((data, index) => (
                            <li key={index}>{data}</li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
};

export default First;
