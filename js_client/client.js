const contentContainer = document.getElementById("content-container");
const loginForm = document.getElementById("login-form");
const searchFormForm = document.getElementById("search-form");
const baseEndpoint = "http://localhost:8000/api";

const handleAuthData = (authData, callback) => {
  localStorage.setItem("access", authData.access);
  localStorage.setItem("refresh", authData.refresh);
  if (callback) {
    callback();
  }
};

const wrtieToContainer = (data) => {
  if (contentContainer) {
    contentContainer.innerHTML =
      "<pre>" + JSON.stringify(data, null, 4) + "</pre>";
  }
};

const getFetchOptions = (method, jsonObject) => ({
  method: method || "GET",
  headers: {
    "Content-Type": "application/json",
    // Authorization: `Bearer ${localStorage.getItem("access")}`,
  },
  body: jsonObject ? JSON.stringify(jsonObject) : null,
});

const isTokenNotValid = (jsonData) => {
  if (jsonData.code && jsonData.code === "token_not_valid") {
    // run a refresh token fetch
    alert("Please login again");
    return false;
  }
  return true;
};

const getProductList = () => {
  const endpoint = `${baseEndpoint}/products/`;
  const accessKey = localStorage.getItem("access");
  const options = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${accessKey}`,
    },
  };
  fetch(endpoint, options)
    .then((response) => response.json())
    .then((data) => {
      const validData = isTokenNotValid(data);
      if (validData) {
        wrtieToContainer(data);
      }
    })
    .catch((err) => {
      console.log("err: ", err);
    });
};

const refreshToken = () => {
  const endpoint = `${baseEndpoint}/token/refresh/`;
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ refresh: localStorage.getItem("refresh") }),
  };
  fetch(endpoint, options)
    .then((response) => response.json())
    .then((x) => {
      console.log(x);
      if (x?.access) {
        localStorage.setItem("access", x.access);
      }
      const isValid = isTokenNotValid(x);
      if (isValid) {
        // getProductList();
      }
    });
};

const validateJWTToken = () => {
  const endpoint = `${baseEndpoint}/token/verify/`;
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ token: localStorage.getItem("access") }),
  };
  fetch(endpoint, options)
    .then((response) => response.json())
    .then((x) => {
      console.log(x);
      if (x?.code === "token_not_valid") {
        refreshToken();
      } else {
        // getProductList();
      }
      // refresh token
    });
};

const handleLogin = (e) => {
  e.preventDefault();
  const loginEndpoint = `${baseEndpoint}/token/`;
  let loginFormData = new FormData(loginForm);
  let loginObjectData = Object.fromEntries(loginFormData);
  fetch(loginEndpoint, getFetchOptions("POST", loginObjectData))
    .then((response) => {
      return response.json();
    })
    .then((authData) => {
      handleAuthData(authData, getProductList);
    })
    .catch((err) => {
      console.log("err: ", err);
    });
};

const handleSearch = () => {
  e.preventDefault();
  const endpoint = `${baseEndpoint}/search/`;
  let searchFormData = new FormData(searchForm));
  let searchObjectData = Object.fromEntries(searchFormData);
  fetch(endpoint, getFetchOptions("POST", searchObjectData))
    .then((response) => {
      return response.json();
    })
    .then((authData) => {
      handleAuthData(authData, getProductList);
    })
    .catch((err) => {
      console.log("err: ", err);
    });
};

document.addEventListener("DOMContentLoaded", () => {
  validateJWTToken();

  if (loginForm) {
    // handle this login form
    loginForm.addEventListener("submit", handleLogin);
  }
  if (searchForm) {
    // handle this login form
    // searchForm.addEventListener("submit", handleSearch);
  }
});
