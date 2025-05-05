// Sample data for dynamic dropdowns
const data = {
    countries: {
      India: { 
        states: { 
          "Kerala": ["Thiruvananthapuram", "Kollam","Pathanamthitta","Alappuzha","Kottayam","Idukki",
                      "Ernakulam","Thrissur","Palakkad","Malappuram","Kozhikode","Wayanad","Kannur","Kasaragod"],
          "Karnataka": ["Bangalore", "Mysore", "Mangalore", "Hubli","Other"],
          "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli","Erode","Salem","Other"],
          "Andhra Pradesh": ["Visakhapatnam", "Vijayawada", "Guntur", "Tirupati","Other"],
          "Other State":["Other City"]
        } 
      },
      Arab: { 
        states: { 
          "Riyadh Region": ["Riyadh", "Al Kharj", "Al Majma'ah", "Diriyah"], 
          "Makkah Region": ["Jeddah", "Mecca", "Taif", "Rabigh"],
          "Eastern Province": ["Dammam", "Al Khobar", "Dhahran", "Jubail"],
          "Other State":["Other City"]
        } 
      },
      USA: { 
        states: { 
          "California": ["Los Angeles", "San Francisco", "San Diego", "Sacramento"], 
          "Texas": ["Houston", "Austin", "Dallas", "San Antonio"],
          "New York": ["New York City", "Buffalo", "Rochester", "Albany"],
          "Florida": ["Miami", "Orlando", "Tampa", "Jacksonville"],
          "Other State":["Other City"]
        } 
      },
      Other: {
        states: {
            "Other State":["Other City"]
        }
      }
    },
  };
  
  const countrySelect = document.getElementById("country");
  const stateSelect = document.getElementById("state");
  const citySelect = document.getElementById("city");
  
  // Populate the country dropdown
  function populateCountries() {
    for (let country in data.countries) {
      const option = document.createElement("option");
      option.value = country;
      option.textContent = country;
      countrySelect.appendChild(option);
    }
  }
  
  // Handle country selection
  countrySelect.addEventListener("change", function () {
    stateSelect.innerHTML = '<option value="">Select the state</option>';
    citySelect.innerHTML = '<option value="">Select the city</option>';
    stateSelect.disabled = true;
    citySelect.disabled = true;
  
    const selectedCountry = countrySelect.value;
    if (selectedCountry && data.countries[selectedCountry]) {
      populateStates(selectedCountry);
      stateSelect.disabled = false;
    }
  });
  
  function populateStates(country) {
    const states = data.countries[country].states;
    for (let state in states) {
      const option = document.createElement("option");
      option.value = state;
      option.textContent = state;
      stateSelect.appendChild(option);
    }
  }
  
  // Handle state selection
  stateSelect.addEventListener("change", function () {
    citySelect.innerHTML = '<option value="">Select the city</option>';
    citySelect.disabled = true;
  
    const selectedState = stateSelect.value;
    const selectedCountry = countrySelect.value;
  
    if (selectedState && data.countries[selectedCountry].states[selectedState]) {
      populateCities(selectedCountry, selectedState);
      citySelect.disabled = false;
    }
  });
  
  function populateCities(country, state) {
    const cities = data.countries[country].states[state];
    cities.forEach(city => {
      const option = document.createElement("option");
      option.value = city;
      option.textContent = city;
      citySelect.appendChild(option);
    });
  }
  
  populateCountries();
  