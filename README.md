This is a contact manager with the options to add, view, search, delete and update contact information namely, Name, Phone1, Phone2, EMail, Whatsapp, Linkedin, Instagram, Facebook.
WE have uploaded the project report with the name DSA(4).

Data Structure Selection and Justification
 Chosen Data Structure: List of Dictionaries
 Justification:
 1. Dictionary for Field-Value Mapping:
 • Each contact is represented as a dictionary with key-value pairs (Name, Phone1,
 Phone2, Email, etc.)
 • Provides O(1) average-case access to individual fields by name
 • Makes code readable and maintainable as fields are accessed by meaningful names
 rather than indices
 2. List for Multiple Records:
 • Alist contains multiple contact dictionaries, maintaining insertion order
 • Allows dynamic growth as contacts are added without pre-allocating size
 • Supports iteration for operations like view, search, update, and delete
 3. CSV Compatibility:
 • Python’s csv.DictReader and csv.DictWriter work seamlessly with dictionar
ies
 • Dictionary keys map directly to CSV column headers
 • Enables easy persistence and data exchange in a human-readable format
 The list of dictionaries structure combines the benefits of structured records (dictio
naries) with ordered collection management (lists), making it ideal for CRUD operations
 on tabular data stored in CSV format


  Search Algorithm Selection and Justification
 Chosen Algorithm: Linear Search (Sequential Search)
 Justification :
 1. Unsorted Data Structure:
 • CSV file maintains insertion order without any sorting
 • Contact records are not organized by any particular field
 • Binary search requires sorted data (O(log n)), which would necessitate sorting
 overhead (O(n log n))
 • For unsorted data, linear search is the natural and most efficient choice
 2. Small Dataset Characteristics:
 • Contact managers typically handle hundreds to low thousands of records
 • Linear search time complexity O(n) is acceptable for small n
 • The simplicity of implementation outweighs the performance benefits of complex
 search algorithms for this scale
 • No additional data structure overhead (like hash tables or trees) required
 3. Multi-field Search Requirement:
 • The search function checks query against ALL fields (Name, Phone, Email, etc.)
 • This flexible, keyword-based search would be difficult with indexed structures
 optimized for single-field lookups
 • Linear search naturally supports checking multiple conditions per iteration
 • Implementation: any(query.lower() in str(value).lower() for value in
 row.values())
 4. CSV File-based Storage:
 • Reading from CSV requires sequential access anyway
 • No in-memory index structure is maintained between operations
 • Each search operation reads the file from start to finish
 • Linear search aligns with the sequential nature of file I/O
 Linear search is optimal for this application because the data is unsorted, the dataset
 is small, searches span multiple fields, and the file-based storage model naturally supports
 sequential access. Alternative algorithms like binary search or hash-based lookups would
 require additional overhead without providing meaningful performance benefits.
