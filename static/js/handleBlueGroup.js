const handleBlueGroup = (action) => {
  // Get the corresponding action and messages
  const refs = handleConstants(action);

  const blueGroupName = document.getElementById(
    'bluegroup-tab-bluegroup-name-text-input'
  );
  const blueGroupDescription = document.getElementById(
    'bluegroup-description-text-input'
  );
  const blueGroupToggle = document.getElementById('bluegroup-tab-toggle');
  const w3Email = document.getElementById('w3-email-text-input');
  const w3Password = document.getElementById('w3-password-text-input');

  handleRequest({
    url: '/bluegroup',
    method: 'POST',
    data: {
      action: refs.action,
      blueGroupName: blueGroupName.value,
      blueGroupDescription: blueGroupDescription.value,
      blueGroupToggle: blueGroupToggle.checked,
      w3Email: w3Email.value,
      w3Password: w3Password.value,
    },
    successCallback: () => {
      displayModal(true, refs.messages.SUCCESS);
    },
    errorCallback: () => displayModal(false, refs.messages.ERROR),
    clickedButtonRef: refs.action,
  });
};
