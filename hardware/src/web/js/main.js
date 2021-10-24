const router = {
	'goToHome': '/index.html',
	'goToAjout': '/pages/ajout.html',
	'goToDebit': '/pages/debit.html',
	'goToNfc': '/pages/nfc.html',
	'goToUnvalidTransac': '/pages/unvalidTransac.html',
	'goToValidTransac': '/pages/validTransac.html',
	'goToAdmin': '/pages/nfc.html?target=/pages/admin.html',
	'goToStats': '/pages/stats.html',
	'goToHisto': '/pages/histo.html',
	'goToSelect': '/pages/nfc.html?target=/pages/consoSelect.html',
};

/**
 * Change la page courante sur une url donnée
 * @param url url a charger
 */
function goTo(url) {
	if (window.location.href.includes('reversed'))
		window.location.replace(url + '?reversed=true');
	else
		window.location.replace(url);
}

/**
 * Permet de charger une page à partir de son identifiant et avec des paramètres dans l'url
 * @param pageId identifiant de la page a charger (Un des noms présent dans router)
 */
function goToWithParam(pageID, params) {
	const element = router[pageID];
	if (element == null)
		throw 'Page doest not exists';
	if (window.location.href.includes('reversed'))
		params += "&reversed=true";
	window.location.replace(element + params);
}

/**
 * Permet d'attendre une durée précise
 */
const delay = async (duration) => new Promise((resolve) => setTimeout(() => resolve(), duration));

eel.expose(prompt_alerts);
/**
 * Fonction permettant d'afficher une alerte à l'écran
 * 
 * @param description message à afficher dans l'alerte
 */
function prompt_alerts(description) {
	alert(description);
}


eel.expose(get_current_url);

/**
 * Fonction permettant de récupérer l'url de la page courante
 * 
 * @return l'url en question
 */
function get_current_url() {
	return window.location.href;
}

/**
 * Permet de récupérer les données stockées dans ue url donnée
 * @param url a parser
 * @return objet contenant les parmètre d'url
 */
function parseURLParams(url) {
	var queryStart = url.indexOf('?') + 1,
		queryEnd = url.indexOf('#') + 1 || url.length + 1,
		query = url.slice(queryStart, queryEnd - 1),
		pairs = query.replace(/\+/g, ' ').split('&'),
		parms = {},
		i, n, v, nv;

	if (query === url || query === '') return;

	for (i = 0; i < pairs.length; i++) {
		nv = pairs[i].split('=', 2);
		n = decodeURIComponent(nv[0]);
		v = decodeURIComponent(nv[1]);

		if (!parms.hasOwnProperty(n)) parms[n] = [];
		parms[n].push(nv.length === 2 ? v : null);
	}
	return parms;
}

/**
 * Fonction permettant de formater une donnée de prix
 * pour l'afficher proprement à l'écran
 * 
 * @param price prix à mettre au bon format
 * @return un string formaté pour le prix
 */
function getPriceString(price) {
	if ((price / 100) % 1 != 0) {
		//decimal number
		return (price / 100) + '0€';
	} else {
		// non decimal number
		return (price / 100) + '.00€';
	}
}

for (let route of Object.keys(router)) {
	const element = document.getElementById(route);
	if (element == null)
		continue;
	element.addEventListener('click', () => goTo(router[route]));
}

if(parseURLParams(window.location.href))
	if (parseURLParams(window.location.href)['reversed'] != undefined)
		document.getElementsByTagName('html')[0].style = 'transform: rotate(180deg);'

