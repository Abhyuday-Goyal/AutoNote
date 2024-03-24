/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      colors:{
        textColor: '#F4F4F4',
        headerColor: "#c00f0f",
        primary: "#02183C",
        secondary: "#CC5F00",
        sidebar: '#e85a5a;',
        active_nav_link : '#1947ee'
      }
    },
    fontFamily: {
      'karla': 'Karla',
    }
  },
  plugins: [],
}

