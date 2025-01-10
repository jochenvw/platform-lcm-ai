Stuff to be built:

- [ ] Ingestion flow
    - Reads sources (delta only)
    - Creates digest of these
    - Store locally in data folder
- [ ] Resoning flow
    - for each persona:
        - read context/digest/memory
        - reason what/how stuff would be applicable / actions can be done
        - store in file (queue)
- [ ] Action flow
    - Read notifications
    - Decide and act


