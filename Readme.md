<a name="readme-top"></a>

[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="static/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">MultPDFGPT</h3>

  <p align="center">
    A Chat Bot using OpenAI to ask questions using your PDFs!
    <br />
    <br />
     <a href="https://mumarj-multipdfgpt.streamlit.app/">Check it out online here! (OpenAI Key needed)</a>
    <!--·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a> -->
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Demo Gif][demo-gif]

<!-- GETTING STARTED -->
## Getting Started

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get your OpenAI API Key [here](https://platform.openai.com/account/api-keys)
2. Clone the repo
3. Install packages, ideally in a virtual environment with Python 3.10
   ```sh
   pip install -r requirements.txt
   ```
4. (Optional) Copy `.env.sample`, rename it to `.env` and enter your API key
   ```js
   OPENAI_API_KEY = 'ENTER YOUR API';
   ```
   Doing this will make the app stop asking for your key on refresh.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1. `Attach PDF` document or `PDF documents` using the `sidebar` to use as context
2. Click `Submit`
3. Type your `query` in main chat area
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add dynamic OpenAI API key support
- [x] Add OpenAI API key validation
- [ ] Add VectorDB (Qdrant)
- [ ] Allow session storage for Chat History
- [ ] Setup account registration
    - [ ] Website Sign Up
    - [ ] Social Sign Up

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

M. Umar Jahangir - [@Linkedin](https://linkedin.com/in/mumarj) - umarjh96@gmail.com
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Flaticon](https://www.flaticon.com)
* [Streamlit](https://www.flaticon.com)
* [LangChain](https://www.langchain.com/)
* [OpenAI](https://platform.openai.com/docs/api-reference)
* [QDrant](https://qdrant.tech/)
* [Python](https://www.python.org/downloads/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[demo-gif]: ./MultPDFGPT-Demo.gif
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/mumarj
