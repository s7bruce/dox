





GET users('{userId}')/onlineMeetings('{meetingId}')/recordings('{recordingId}')/content





# {
#   "@odata.context": "https://graph.microsoft.com/beta/$metadata#Collection(callTranscript)",
#   "@odata.count": 2,
#   "@odata.nextLink": "https://graph.microsoft.com/beta/users('{userId}')/onlineMeetings/getAllTranscripts?$filter=MeetingOrganizerId+eq+%27{userId}%27&$skiptoken=MSMjMCMjTkNaYVNIQjVVbXRPYWxaV1dscGFWVGg1V2pOb1IxUXpRWGxrUm1oTFVrWmtTV1ZyYkhwUlZVWm9UMWR3VEdWWGRFTlJWVVpDVVZFOVBRPT0%3d",
#   "value":
#     [
#       {
#        "@odata.type": "#microsoft.graph.callTranscript",
#        "id": "MSMjMCMjMGFjNmUwZTgtYmZjYy00NDQxLTk2MGYtZjllNjVhNjI0NzBh",
#        "meetingId": "MSoxMjczYTAxNi0yMDFkLTRmOTUtODA4My0xYjdmOTliM2VkZWIqMCoqMTk6bWVldGluZ19aR1F3WTJZNE9XTXROekppWlMwME1XWTRMVGc0TWpBdE1ERXdOV1kzWlRsak9UTXlAdGhyZWFkLnYy",
#        "meetingOrganizerId": "{userId}",
#        "transcriptContentUrl": "https://graph.microsoft.com/beta/users/{userId}/onlineMeetings/MSoxMjczYTAxNi0yMDFkLTRmOTUtODA4My0xYjdmOTliM2VkZWIqMCoqMTk6bWVldGluZ19aR1F3WTJZNE9XTXROekppWlMwME1XWTRMVGc0TWpBdE1ERXdOV1kzWlRsak9UTXlAdGhyZWFkLnYy/transcripts/MSMjMCMjMGFjNmUwZTgtYmZjYy00NDQxLTk2MGYtZjllNjVhNjI0NzBh/content",
#       "createdDateTime": "2022-08-03T20:43:36.6248355Z"
#       },
#       {
#        "@odata.type": "#microsoft.graph.callTranscript",
#        "id": "{transcriptId}",
#        "meetingId": "{meetingId}",
#        "meetingOrganizerId": "{userId}",
#        "transcriptContentUrl": "https://graph.microsoft.com/beta/users/{userId}/onlineMeetings/{meetingId}/transcripts/{transcriptId}/content",
#        },
#      ]
#     }