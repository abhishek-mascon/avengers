
var axios = require('axios');

module.exports = {

	post: function (url, params, authenticated=false) {
		var access_token = "Token " + localStorage.getItem('avengers_secret');
		var headers = {headers: {}};
		if(authenticated) {
			headers.headers = {Authorization: access_token};
		}
		return axios.post(url, params, headers)
		.then(function (response) {
			response.success = true;
			return response;
		})
		.catch(function (err) {
			err.response.data.success = false;
			return err.response.data;
		});
	},

	get: function (url, authenticated=false) {
		var access_token = "Token " + localStorage.getItem('avengers_secret');
		var headers = {headers: {}};
		if(authenticated) {
			headers.headers = {Authorization: access_token};
		}
		return axios.get(url, headers)
		.then(function (response) {
			response.success = true;
			return response;
		})
		.catch(function (err) {
			err.response.data.success = false;
			return err.response.data;
		});
	},

	sign_up: function (form_data) {
		var url = 'rest-auth/registration/';
		var params = {
			username: form_data.username,
			password1: form_data.password1,
			password2: form_data.password2,
			email: form_data.email
		};
		return this.post(url, params);
	},

	login: function (form_data) {
		var url = 'rest-auth/login/';
		var params = {
			username: form_data.username,
			password: form_data.password
		};
		return this.post(url, params);
	},

	addToFolio: function (items) {
		var url = 'fury/portfolio/add/';
		var params = {
			items: items
		};
		return this.post(url, params, true);
	},

	load_stocks: function () {
		var url = 'fury/stocks';
		this.get(url, true)
		.then(function (response) {
			var symbols = [];
			response.data.map((stock) => {
				symbols.push({label: stock['symbol'], value: stock['id']});
			});
			localStorage.setItem('stocks', JSON.stringify(symbols));
		});
	},

	getPortfolio: function () {
		this.load_stocks();
		var url = 'fury/portfolio/get';
		return this.get(url, true);
	}

}