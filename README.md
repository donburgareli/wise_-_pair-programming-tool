Wise - A Pair-Programming Assistant Tool
-----------

Wise is an open-source initiative aimed at enhancing collaboration and productivity among developers through pair programming. The project utilizes AutoGen AI Agents and the GPT4Free interference API to provide a cost-free AI assistant that facilitates real-time collaboration and code improvement.

Wise uses natural language processing to understand developers' queries, code snippets, and challenges. This enables it to offer helpful suggestions, perform code analysis, and assist with debugging, thereby smoothing pair programming sessions.

Furthermore, Wise integrates automated code generation features powered by AutoGen AI Agents to simplify repetitive tasks and minimize manual effort. By automating routine coding tasks, developers can allocate more time to the creative and challenging aspects of their projects.

Currently, Wise is in its early stages of development. I'm actively refining and expanding its features to better serve the programming community.

Planned Features:
-----------

* Enhance natural language processing capabilities for better understanding of developer queries
* Expand code analysis and debugging assistance functionalities
* Integrate additional automation features to further streamline pair programming sessions
* Conduct thorough testing and debugging to ensure stability and reliability
* Gather feedback from early users to inform future development and improvements
* Document usage guidelines and provide comprehensive support resources

Dependencies
-----------
- Python 3.12.2
- GPT4Free: https://github.com/xtekky/gpt4free
- AutoGen: https://github.com/microsoft/autogen
  
Installation
-----------
1. Clone this repository:
   ```
   git clone https://github.com/donburgareli/wise-pair-programming-tool.git
   ```

2. Create conda environment
   ```
   conda create -n wise python=3.12.2
   ```
   
3. Activate conda environment
   ```
   conda activate wise
   ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Install g4f api and pyautogen:
   ```
   pip install g4f[api]
   pip install pyautogen
   ```
   Be sure to check the repositories for more information / setup proccesses.
   
Usage
-----------
1. Navigate to the project directory:
   ```
   cd wise-pair-programming-tool
   ```

2. Activate conda environment
   ```
   conda activate wise
   ```

3. Run the Python script:
   ```
   python app.py
   ```

Contributing
-----------
Contributions are welcome! Here's how you can contribute:
- Fork the repository
- Create your feature branch (`git checkout -b feature/YourFeature`)
- Commit your changes (`git commit -am 'Add some feature'`)
- Push to the branch (`git push origin feature/YourFeature`)
- Create a new Pull Request

License
-----------

MIT License
