const handleAdministrator = (action) => {
  // Get the corresponding action and messages
  const refs = handleConstants(action);

  const administratorToggle = document.getElementById(
    'administrator-tab-toggle'
  );
  const blueGroupName = document.getElementById(
    'administrator-tab-bluegroup-name-text-input'
  );
  const userId = document.getElementById('administrator-tab-uid-text-input');
  const w3Email = document.getElementById('w3-email-text-input');
  const w3Password = document.getElementById('w3-password-text-input');

  handleRequest({
    url: '/administrator',
    method: 'POST',
    data: {
      action: refs.action,
      administratorToggle: administratorToggle.checked,
      blueGroupName: blueGroupName.value,
      userId: userId.value,
      w3Email: w3Email.value,
      w3Password: w3Password.value,
    },
    successCallback: () => displayModal(true, refs.messages.SUCCESS),
    errorCallback: () => displayModal(false, refs.messages.ERROR),
    clickedButtonRef: refs.action,
  });
};
