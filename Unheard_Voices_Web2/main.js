var typed= new Typed(".text", {
    strings: ["Empowering you to connect and thrive!", "Empowering you to connect and thrive!", "Empowering you to connect and thrive!"],
    typeSpeed: 100,
    backSpeed: 100,
    backDelay: 1000,
    loop: true,
});

const languages = [
  {
    no: "16",
    name: "English",
    native: "English",
    code: "en",
  },
  {
    no: "1",
    name: "Afrikaans",
    native: "Afrikaans",
    code: "af",
  },
  {
    no: "2",
    name: "Albanian",
    native: "Shqip",
    code: "sq",
  },
  {
    no: "3",
    name: "Arabic",
    native: "عربي",
    code: "ar",
  },
  {
    no: "4",
    name: "Armenian",
    native: "Հայերէն",
    code: "hy",
  },
  {
    no: "5",
    name: "Azerbaijani",
    native: "آذربایجان دیلی",
    code: "az",
  },
  {
    no: "6",
    name: "Basque",
    native: "Euskara",
    code: "eu",
  },
  {
    no: "7",
    name: "Belarusian",
    native: "Беларуская",
    code: "be",
  },
  {
    no: "8",
    name: "Bulgarian",
    native: "Български",
    code: "bg",
  },
  {
    no: "9",
    name: "Catalan",
    native: "Català",
    code: "ca",
  },
  {
    no: "10",
    name: "Chinese (Simplified)",
    native: "中文简体",
    code: "zh-CN",
  },
  {
    no: "11",
    name: "Chinese (Traditional)",
    native: "中文繁體",
    code: "zh-TW",
  },
  {
    no: "12",
    name: "Croatian",
    native: "Hrvatski",
    code: "hr",
  },
  {
    no: "13",
    name: "Czech",
    native: "Čeština",
    code: "cs",
  },
  {
    no: "14",
    name: "Danish",
    native: "Dansk",
    code: "da",
  },
  {
    no: "15",
    name: "Dutch",
    native: "Nederlands",
    code: "nl",
  },
  {
    no: "17",
    name: "Estonian",
    native: "Eesti keel",
    code: "et",
  },
  {
    no: "18",
    name: "Filipino",
    native: "Filipino",
    code: "tl",
  },
  {
    no: "19",
    name: "Finnish",
    native: "Suomi",
    code: "fi",
  },
  {
    no: "20",
    name: "French",
    native: "Français",
    code: "fr",
  },
  {
    no: "21",
    name: "Galician",
    native: "Galego",
    code: "gl",
  },
  {
    no: "22",
    name: "Georgian",
    native: "ქართული",
    code: "ka",
  },
  {
    no: "23",
    name: "German",
    native: "Deutsch",
    code: "de",
  },
  {
    no: "24",
    name: "Greek",
    native: "Ελληνικά",
    code: "el",
  },
  {
    no: "25",
    name: "Haitian Creole",
    native: "Kreyòl ayisyen",
    code: "ht",
  },
  {
    no: "26",
    name: "Hebrew",
    native: "עברית",
    code: "iw",
  },
  {
    no: "27",
    name: "Hindi",
    native: "हिन्दी",
    code: "hi",
  },
  {
    no: "28",
    name: "Hungarian",
    native: "Magyar",
    code: "hu",
  },
  {
    no: "29",
    name: "Icelandic",
    native: "Íslenska",
    code: "is",
  },
  {
    no: "30",
    name: "Indonesian",
    native: "Bahasa Indonesia",
    code: "id",
  },
  {
    no: "31",
    name: "Irish",
    native: "Gaeilge",
    code: "ga",
  },
  {
    no: "32",
    name: "Italian",
    native: "Italiano",
    code: "it",
  },
  {
    no: "33",
    name: "Japanese",
    native: "日本語",
    code: "ja",
  },
  {
    no: "34",
    name: "Korean",
    native: "한국어",
    code: "ko",
  },
  {
    no: "35",
    name: "Latvian",
    native: "Latviešu",
    code: "lv",
  },
  {
    no: "36",
    name: "Lithuanian",
    native: "Lietuvių kalba",
    code: "lt",
  },
  {
    no: "37",
    name: "Macedonian",
    native: "Македонски",
    code: "mk",
  },
  {
    no: "38",
    name: "Malay",
    native: "Malay",
    code: "ms",
  },
  {
    no: "39",
    name: "Maltese",
    native: "Malti",
    code: "mt",
  },
  {
    no: "40",
    name: "Norwegian",
    native: "Norsk",
    code: "no",
  },
  {
    no: "41",
    name: "Persian",
    native: "فارسی",
    code: "fa",
  },
  {
    no: "42",
    name: "Polish",
    native: "Polski",
    code: "pl",
  },
  {
    no: "43",
    name: "Portuguese",
    native: "Português",
    code: "pt",
  },
  {
    no: "44",
    name: "Romanian",
    native: "Română",
    code: "ro",
  },
  {
    no: "45",
    name: "Russian",
    native: "Русский",
    code: "ru",
  },
  {
    no: "46",
    name: "Serbian",
    native: "Српски",
    code: "sr",
  },
  {
    no: "47",
    name: "Slovak",
    native: "Slovenčina",
    code: "sk",
  },
  {
    no: "48",
    name: "Slovenian",
    native: "Slovensko",
    code: "sl",
  },
  {
    no: "49",
    name: "Spanish",
    native: "Español",
    code: "es",
  },
  {
    no: "50",
    name: "Swahili",
    native: "Kiswahili",
    code: "sw",
  },
  {
    no: "51",
    name: "Swedish",
    native: "Svenska",
    code: "sv",
  },
  {
    no: "52",
    name: "Thai",
    native: "ไทย",
    code: "th",
  },
  {
    no: "53",
    name: "Turkish",
    native: "Türkçe",
    code: "tr",
  },
  {
    no: "54",
    name: "Ukrainian",
    native: "Українська",
    code: "uk",
  },
  {
    no: "55",
    name: "Urdu",
    native: "اردو",
    code: "ur",
  },
  {
    no: "56",
    name: "Vietnamese",
    native: "Tiếng Việt",
    code: "vi",
  },
  {
    no: "57",
    name: "Welsh",
    native: "Cymraeg",
    code: "cy",
  },
  {
    no: "58",
    name: "Yiddish",
    native: "ייִדיש",
    code: "yi",
  },
];

const languagesVoices = 
[
    {name: 'US English Female'},
    
    {name: 'US English Male'},
    
    {name: 'Arabic Male'},
    
    {name: 'Arabic Female'},
    
    {name: 'Armenian Male'},
    
    {name: 'Australian Female'},
    
    {name: 'Australian Male'},
    
    {name: 'Bangla Bangladesh Female'},
    
    {name: 'Bangla Bangladesh Male'},
    
    {name: 'Bangla India Female'},
    
    {name: 'Bangla India Male'},
    
    {name: 'Brazilian Portuguese Female'},
    
    {name: 'Chinese Female'},
    
    {name: 'Chinese Male'},
    
    {name: 'Chinese (Hong Kong) Female'},
    
    {name: 'Chinese (Hong Kong) Male'},
    
    {name: 'Chinese Taiwan Female'},
    
    {name: 'Chinese Taiwan Male'},
    
    {name: 'Czech Female'},
    
    {name: 'Danish Female'},
    
    {name: 'Deutsch Female'},
    
    {name: 'Deutsch Male'},
    
    {name: 'Dutch Female'},
    
    {name: 'Dutch Male'},
    
    {name: 'Estonian Male'},
    
    {name: 'Filipino Female'},
    
    {name: 'Finnish Female'},
    
    {name: 'French Female'},
    
    {name: 'French Male'},
    
    {name: 'French Canadian Female'},
    
    {name: 'French Canadian Male'},
    
    {name: 'Greek Female'},
    
    {name: 'Hindi Female'},
    
    {name: 'Hindi Male'},
    
    {name: 'Hungarian Female'},
    
    {name: 'Indonesian Female'},
    
    {name: 'Indonesian Male'},
    
    {name: 'Italian Female'},
    
    {name: 'Italian Male'},
    
    {name: 'Japanese Female'},
    
    {name: 'Japanese Male'},
    
    {name: 'Korean Female'},
    
    {name: 'Korean Male'},
    
    {name: 'Latin Male'},
    
    {name: 'Nepali'},
    
    {name: 'Norwegian Female'},
    
    {name: 'Norwegian Male'},
    
    {name: 'Polish Female'},
    
    {name: 'Polish Male'},
    
    {name: 'Portuguese Female'},
    
    {name: 'Portuguese Male'},
    
    {name: 'Romanian Female'},
    
    {name: 'Russian Female'},
    
    {name: 'Sinhala'},
    
    {name: 'Slovak Female'},
    
    {name: 'Spanish Female'},
    
    {name: 'Spanish Latin American Female'},
    
    {name: 'Spanish Latin American Male'},
    
    {name: 'Swedish Female'},
    
    {name: 'Swedish Male'},
    
    {name: 'Tamil Female'},
    
    {name: 'Tamil Male'},
    
    {name: 'Thai Female'},
    
    {name: 'Thai Male'},
    
    {name: 'Turkish Female'},
    
    {name: 'Turkish Male'},
    
    {name: 'Ukrainian Female'},
    
    {name: 'Vietname:se Female'},
    
    {name: 'Vietname:se Male'},
    
    {name: 'Afrikaans Male'},
    
    {name: 'Albanian Male'},
    
    {name: 'Bosnian Male'},
    
    {name: 'Catalan Male'},
    
    {name: 'Croatian Male'},
    
    {name: 'Esperanto Male'},
    
    {name: 'Icelandic Female'},
    
    {name: 'Latvian Male'},
    
    {name: 'Macedonian Male'},
    
    {name: 'Moldavian Female'},
    
    {name: 'Montenegrin Male'},
    
    {name: 'Serbian Male'},
    
    {name: 'Serbo-Croatian Male'},
    
    {name: 'Swahili Male'},
    
    {name: 'Welsh Male'},
    
    {name: 'Fallback UK'},
    
];

let SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
let recognition;
let recording = false;

const recordbtn = document.querySelector(".btn-record"),
    outputsection = document.querySelector(".output-section"),
    inputField = document.querySelector(".text-input"),
    inputLanguage = document.querySelector("#language-write"),
    outputLanguage = document.querySelector("#language-read");

function populateLanguages() {
    languages.forEach((lang) => {
      const option = document.createElement("option");
      option.value = lang.code;
      option.innerHTML = lang.name;
      inputLanguage.appendChild(option);
    });
  }
  
  populateLanguages();
  
function populateLanguagesVoices()
{
    languagesVoices.forEach((lang) => {
        var option = document.createElement("option");
        option.value = lang.name;
        option.innerHTML = lang.name;
        outputLanguage.appendChild(option);
    });
}
  
populateLanguagesVoices();

function createNewRecoSection(inputValue)
{
    let recosection2 = document.createElement("div");
    let voiceIcon2 = document.createElement("span");
    let xIcon2 = document.createElement("span");

    recosection2.setAttribute("contenteditable","true")

    voiceIcon2.innerHTML = `<ion-icon name="volume-medium-outline"></ion-icon>`;
    xIcon2.innerHTML = `<ion-icon name="close-circle-outline"></ion-icon>`;
    recosection2.className = "reco-section";
    voiceIcon2.className = "voice-icon";
    xIcon2.className = "x-icon";

    recosection2.appendChild(voiceIcon2);
    recosection2.appendChild(xIcon2);
    recosection2.appendChild(document.createTextNode(inputValue));

    outputsection.appendChild(recosection2);

    voiceIcon2.addEventListener("click", function () {
        var text = recosection2.textContent.trim();
        if (text !== '') {
            responsiveVoice.speak(text, outputLanguage.value);
        }
    });

    xIcon2.addEventListener("click", function () {
        outputsection.removeChild(recosection2);
    });
    recosection2.setAttribute("dir", detectLanguageDirection(inputField.value));
    outputsection.scrollTop = outputsection.scrollHeight;

    if (inputLanguage.value == 'ar') {
        recosection2.setAttribute("dir", "rtl");
    }
}



document.addEventListener("DOMContentLoaded", function () {

    inputField.addEventListener('keydown', function (event) {
        if (event.key === 'Enter') {
            const inputValue = inputField.value.trim();
            if (inputValue !== '') {
                createNewRecoSection(inputValue);
            }
            inputField.value = '';
        }
    });

    recordbtn.addEventListener("click", () => {
        if (!recording) {
            startSpeechToText();
            recording = true;
        } else {
            stopRecording();
        }
    });

  

    function startSpeechToText() {
        try {
            recognition = new SpeechRecognition();
            // Add your language selection logic here, assuming `inputLanguage` is an input element
            recognition.lang = inputLanguage.value;
            recognition.interimResults = true;
            recordbtn.classList.add("recording");
            // Assuming there is a <p> inside the recordbtn to display status

            recognition.start();
            recognition.onresult = (event) => {
                const speechResult = event.results[0][0].transcript;
                if (event.results[0].isFinal) {
                    
                    createNewRecoSection(speechResult);
                } else {
                    // if (!document.querySelector(".interim")) {
                    //     const interim = document.createElement("p");
                    //     interim.classList.add("interim");
                    //     // Assuming there is a result element to append the interim results
                    //     document.querySelector(".output-section").appendChild(interim);
                    // }
                    // document.querySelector(".interim").innerHTML = " " + speechResult;
                }
            };
            recognition.onspeechend = () => {
                startSpeechToText();
            };
            recognition.onerror = (event) => {
                stopRecording();
                if (event.error === "no-speech") {
                    alert("No speech was detected. Stopping...");
                } else if (event.error === "audio-capture") {
                    alert("No microphone was found. Ensure that a microphone is installed.");
                } else if (event.error === "not-allowed") {
                    alert("Permission to use the microphone is blocked.");
                } else if (event.error === "aborted") {
                    alert("Listening Stopped.");
                } else {
                    alert("Error occurred in recognition: " + event.error);
                }
            };
        } catch (error) {
            recording = false;
            console.log(error);
        }
    }

    function stopRecording() {
        if (recognition) {
            recognition.stop();
        }
        recordbtn.classList.remove("recording");
        recording = false;
    }
});

function detectLanguageDirection(text) {
  // Simple check based on Arabic characters
  return /[\u0600-\u06FF]/.test(text) ? "rtl" : "ltr";
}

const camSection = document.querySelector(".cam-section")
const webCamElement = document.getElementById("webCam");
const cambtn = document.querySelector(".btn-cam");
const canvasElement = document.getElementById("canvas");
let isCameraOn = false;
const webcam = new Webcam(webCamElement, "user", canvasElement);
var numberFrames = 0;
const frameCount = document.getElementById('frameCount');
const frameCount2 = document.getElementById('frameCount2');
let previousPrediction = '';
let continueSendingFrames = true;

console.log('isCameraOn')


// FPS ----> FramePerSecond

async function startFPS() {
    try {
        var video = document.getElementById('webCam');
        var canvas = document.getElementById('canvas');
        var ctx = canvas.getContext('2d');

        // Set canvas size to match video size
        canvas.width = 480;
        canvas.height = 640;

        // wait until permission to open the camera is ready
        await video.play();

        // Draw the current frame onto the canvas
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

        // Get image data from the canvas
        var imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);

        // Convert the image data to bytes (Uint8Array)
        var bytes = new Uint8Array(imageData.data);

        // Specify the server URL
        var serverURL = 'http://192.168.245.224:3000/upload';

        // Check if we should continue sending frames
        if (continueSendingFrames) {
            // Send frames to the server and handle predictions asynchronously
            await sendFramesAndPredict(serverURL, bytes);
        }

    } catch (error) {
        console.error(error);
    } finally {
        // Continue capturing frames if the video is playing
        var video = document.getElementById('webCam');
        
        if (!video.paused && !video.ended && continueSendingFrames) {
            // numberFrames++;
            // frameCount.textContent = `Frames Captured: ${numberFrames}`;
            requestAnimationFrame(startFPS);
        }
    }
}

async function sendFramesAndPredict(serverURL, bytes) {
    try {
        const response = await fetch(serverURL, {
            method: 'POST',
            body: bytes,
        });

        // Log the status and response text for debugging
        console.log('Response Status:', response.status);

        if (!response.ok) {
            console.error('Server returned an error:', response.status);
            return;
        }

        const data = await response.json();
        const newPrediction = data.message;

        console.log('New Prediction:', newPrediction);

        // Update the HTML element only if the new prediction is not null
        if (newPrediction !== null && newPrediction.trim() !== '') {
            // Add a space between each word
            previousPrediction += newPrediction + ' ';
            inputField.value = previousPrediction.trim();  // trim to remove trailing space
        }

    } catch (error) {
        console.error('Error:', error);
    }
}


cambtn.addEventListener("click", function ()
{
    if (isCameraOn)
    {
        if (inputField.value !== null && inputField.value.trim() !== '') 
        {
            createNewRecoSection(inputField.value);
        }
        continueSendingFrames = false;
        webcam.stop();
        camSection.style.display = "none"
        webCamElement.hidden = true; // Hide the video element
        isCameraOn = false;
        cambtn.classList.remove("cpaturing");
        cambtn.style.background="#DF6BEF"
    }
    else {
        continueSendingFrames = true;
        webcam.start();
        startFPS();
        camSection.style.display = "block"
        cambtn.classList.add("cpaturing");
        cambtn.style.background="#EA7B7B"
        webCamElement.hidden = false; // Show the video element
        isCameraOn = true;
    }
});
