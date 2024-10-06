
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
      extend: {
          keyframes: {
              'fade-up-fake': {
                  '0%': { transform: 'translateY(100%)', opacity: '1' },
                  '100%': { transform: 'translateY(-100%)', opacity: '0' },
              },
              'fade-up-true': {
                  '0%': { transform: 'translateY(100%)', opacity: '1' },
                  '100%': { transform: 'translateY(-100%)', opacity: '0' },
              },
          },
          refine: {
            "0%": {
              left: "0%" , bottom: "20%",
            },
            "25%": {
              left: "40%" , bottom: "20%",
            },
            "50%":{
              left: "60%" , bottom: "20%",
            },
            "75%":{
              left: "75%" , bottom: "20%",
            },
            "100%":{
              right: "0%" , bottom: "20%",
            },
           },
          },
  
          animation: {
              'fade-up-fake': 'fade-up-fake 3s forwards',
              'fade-up-true': 'fade-up-true 3s forwards',
              "refine-slide": "refine 10s infinite",

          },
      },
  },
  {
  plugins: [],
}