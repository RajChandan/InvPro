module.exports = {
  content: [
    "../templates/**/*.html",
    "../**/templates/**/*.html",
    "../../templates/**/*.html",
    "../../core/templates/**/*.html",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'sans-serif'], // For body
        heading: ['Inter', 'sans-serif'],
      },
      colors: {
        primary: {
          DEFAULT: '#0B1F3F',
          50: '#f8f8f8',
          100: '#e8e8e8',
          200: '#d3d3d3',
          300: '#a3a3a3',
          400: '#737373',
          500: '#525252',
          600: '#404040',
          700: '#262626',
          800: '#171717',
          900: '#0a0a0a',
          950: '#030303',
        },
        secondary: {
          DEFAULT: '#2A4B8C',
          50: '#f8f8f8',
          100: '#e8e8e8',
          200: '#d3d3d3',
          300: '#a3a3a3',
          400: '#737373',
          500: '#525252',
          600: '#404040',
          700: '#262626',
          800: '#171717',
          900: '#0a0a0a',
          950: '#030303',
        },
        accent: {
          DEFAULT: '#FFB800',
          50: '#f8f8f8',
          100: '#e8e8e8',
          200: '#d3d3d3',
          300: '#a3a3a3',
          400: '#737373',
          500: '#525252',
          600: '#404040',
          700: '#262626',
          800: '#171717',
          900: '#0a0a0a',
          950: '#030303',
        },
      },
      // You can extend spacing, fonts, animations, etc. as needed
    },
  },
  plugins: [],
};