from datetime import datetime, timedelta, timezone
from aws_xray_sdk.core import xray_recorder

class NotificationsActivities:
  def run():
    try:
      now = datetime.now(timezone.utc).astimezone()
      # X-RAY ---------------------------------------------------------
      # start a segment
      segment = xray_recorder.begin_subsegment('NotificationsActivities-Segment')
      xray_dict = {
      "uuid": '68f126b0-1ceb-4a33-88be-d90fa7109eee',
      "handle":  'Pepe',
      "message": 'I am a black unicorn',
      "created_at": (now - timedelta(days=2)).isoformat(),
      "expires_at": (now + timedelta(days=5)).isoformat(),
      }
      segment.put_metadata('Now',xray_dict,"NotificationsActivities")

      results = [{
        'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
        'handle':  'Pepe',
        'message': 'I am a black unicorn',
        'created_at': (now - timedelta(days=2)).isoformat(),
        'expires_at': (now + timedelta(days=5)).isoformat(),
        'likes_count': 5,
        'replies_count': 1,
        'reposts_count': 0,
        'replies': [{
          'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
          'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
          'handle':  'Worf',
          'message': 'This post has no honor!',
          'likes_count': 0,
          'replies_count': 0,
          'reposts_count': 0,
          'created_at': (now - timedelta(days=2)).isoformat()
        }],
      }
      ]
      try:
        #X-RAY ---------------------------------------------------------
        # Start a subsegment
        subsegment = xray_recorder.begin_subsegment('NotificationsActivities-Subsegment')
        xray_dict['results'] = len(results)
        # Add the metadata to the segment
        subsegment.put_metadata('results', xray_dict, 'NotificationsActivities')
      except Exception as e:
        # Raise the error in the segment
        raise e
      finally:  
        # Close the subsegment
        xray_recorder.end_subsegment()
    except Exception as e:
      # Raise the error in the segment
      raise e
    finally:  
      # Close the segment
      xray_recorder.end_subsegment()
    return results