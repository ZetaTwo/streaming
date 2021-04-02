'use strict';

module.exports = function (nodecg) {
	nodecg.log.info('ZetaTwo loaded');

	const statusRep = nodecg.Replicant('status', { defaultValue: "" });

	const app = nodecg.Router();
	app.post('/zetatwo/status', (req, res) => {
		statusRep.value = req.body.status || '';
		res.json({'status': 'ok'});
	});
	nodecg.mount(app);
};
