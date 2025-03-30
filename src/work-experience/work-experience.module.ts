import { Module } from '@nestjs/common';
import { MongooseModule } from '@nestjs/mongoose';
import { WorkExperienceService } from './work-experience.service';
import { WorkExperienceController } from './work-experience.controller';
import {
  WorkExperience,
  WorkExperienceSchema,
} from './entities/work-experience.entity';

@Module({
  imports: [
    MongooseModule.forFeature([
      { name: WorkExperience.name, schema: WorkExperienceSchema },
    ]),
  ],
  controllers: [WorkExperienceController],
  providers: [WorkExperienceService],
})
export class WorkExperienceModule {}
